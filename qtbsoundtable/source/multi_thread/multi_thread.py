from typing import Callable, Iterable, Mapping, Any, Type, Dict, Tuple, Union
from random import randint
from multiprocessing import Process

from .interfaces import MultiThreadInterface

class MultiThread(MultiThreadInterface):
    def __init__(self, thread_number_limit: int = 10, \
        error_class: Type[Exception] = None) -> None:
        
        self.__process : Dict[int, \
            Tuple[Union[Process, Callable, Iterable, Mapping]]] = {} # Process is a Process object, Callable is a function, Iterable is a list, Mapping is a dict
        self.__thread_number_limit = thread_number_limit
        self.__error_class = error_class

    def create_thread(self, target: Callable = None, \
        args: Iterable[Any] = (), kwargs: Mapping[str, Any] = None, \
        automatic_start: bool = True) -> int:

        if kwargs is None:
            kwargs = {}
        
        process = Process(target=target, args=args, kwargs=kwargs)
        id = randint(1, 100000000)

        self.__process[id] = (process, target, args, kwargs)

        if automatic_start:
            self.start_thread(id)

        return id
    
    def delete_thread(self, id: int) -> None:
        try:
            self.stop_thread(id)
            self.__process.pop(id)
        except KeyError:
            pass

    def start_thread(self, id: int) -> None:
        try:
            if self.is_alive(id):
                self.stop_thread(id)
            
            if self.private__verify_running_threads_number() == \
                self.__thread_number_limit:

                self.stop_all_threads()
                raise self.__error_class("Limit of Threads reached")

            _, target, args, kwargs = self.__process[id]
            new_th = Process(target=target, args=args, kwargs=kwargs)
            self.__process[id] = (new_th, target, args, kwargs)
            new_th.start()

        except KeyError:
            raise self.__error_class("Thread not found")

    def stop_thread(self, id: int) -> None:
        try:
            process = self.__process[id][0]
            process.terminate()
        except KeyError:
            raise self.__error_class("Thread not found")
        except (RuntimeError, AttributeError):
            pass

    def is_alive(self, id: int) -> bool:
        try:
            process = self.__process[id][0]
            return process.is_alive()
        except KeyError:
            raise self.__error_class("Thread not found")

    def private__verify_running_threads_number(self) -> int:
        # Return the number of running threads simultaneously
        number = 1

        for id, _ in self.__process.items():
            if self.is_alive(id):
                number += 1

        return number

    def stop_all_threads(self) -> None:
        print("Alert: Max Threads Reached!!!\nStop all threads!!!")
        while True:

            if self.private__verify_running_threads_number() == 1:
                break

            try:
                for id, _ in self.__process.items():
                    self.stop_thread(id)
            except RuntimeError:
                pass
