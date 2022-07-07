from typing import Callable, Iterable, Mapping, Any, Type, Dict
from random import randint
from threading import Thread

from .interfaces import MultiThreadInterface

class MultiThread(MultiThreadInterface):
    def __init__(self, thread_number_limit: int = 10, \
        error_class: Type[Exception] = None) -> None:
        
        self.__threads : Dict[int, Thread] = {}
        self.__thread_number_limit = thread_number_limit
        self.__error_class = error_class

    def create_thread(self, target: Callable = None, \
        args: Iterable[Any] = ..., kwargs: Mapping[str, Any] = ..., \
        automatic_start: bool = True) -> int:
        
        th = Thread(target=target, args=args, kwargs=kwargs)
        id = randint(1, 100000000)

        if not id in self.__threads:
            self.__threads[id] = th

        if automatic_start:
            if self.private__verify_running_threads_number == \
                self.__thread_number_limit:

                raise self.__error_class("Limit of Threads reached")

            else:
                th.start()

        return id
    
    def delete_thread(self, id: int) -> None:
        try:
            self.__threads.pop(id)
        except KeyError:
            pass

    def start_thread(self, id: int) -> None:
        try:
            th = self.__threads[id]
            self.stop_thread(id)
            th.start()
        except KeyError:
            raise self.__error_class("Thread not found")

    def stop_thread(self, id: int) -> None:
        try:
            th = self.__threads[id]
            th.join()
        except KeyError:
            raise self.__error_class("Thread not found")

    def is_alive(self, id: int) -> bool:
        try:
            th = self.__threads[id]
            return th.is_alive()
        except KeyError:
            raise self.__error_class("Thread not found")

    def private__verify_running_threads_number(self) -> int:
        number = 0

        for thread in self.__threads:
            if thread.is_alive():
                number += 1

        return number
