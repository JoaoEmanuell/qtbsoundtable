from abc import ABC, abstractmethod
from typing import Callable, Iterable, Mapping, Any, Type

class MultiThreadInterface(ABC):
    @abstractmethod
    def __init__(
        self, 
        thread_number_limit:int=10,
        error_class: Type[Exception]=None
        ) -> None:
        """Init

        Args:
            thread_number_limit (int, optional): Concurrent thread limit. Defaults to 10.
            error_class (Type[MultiThreadErrorInterface]): Error class, for emit erros.

        """        
        raise NotImplementedError()

    def create_thread(
        self, 
        target: Callable=None,
        args: Iterable[Any]=(),
        kwargs: Mapping[str, Any]={},
        automatic_start: bool=True
        ) -> int:
        """_summary_

        Args:
            target (Callable): target to thread
            args (Iterable[Any], optional): Args to target. Defaults to ().
            kwargs (Mapping[str, Any], optional): Kwargs to target. Defaults to {}.
            automatic_start (bool, optional): If true, when being created the thread start. Defaults to True.

        Raises:
            MultiThreadErrorInterface: If the thread limit is reached.

        Returns:
            int: Thread id.
        """        
        raise NotImplementedError()
        raise MultiThreadErrorInterface()

    def delete_thread(self, id: int) -> None:
        """Delete Thread

        Args:
            id (int): Thread id.

        """        
        raise NotImplementedError()

    def start_thread(self, id: int) -> None:
        """Start Thread, case the thread be running, restart the thread

        Args:
            id (int): Thread id.

        Raises:
            MultiThreadErrorInterface: Case the thread not found.
        """        
        raise NotImplementedError()
        raise MultiThreadErrorInterface()

    def stop_thread(self, id: int) -> None:
        """Stop Thread

        Args:
            id (int): _description_

        Raises:
            MultiThreadErrorInterface: Case the thread not found.
        """        
        raise NotImplementedError()
        raise MultiThreadErrorInterface()

    def is_alive(self, id: int) -> bool:
        """Is Thread Alive

        Args:
            id (int): Thread id

        Raises:
            MultiThreadErrorInterface: Case the thread not found.

        Returns:
            bool: True if the thread is alive.
        """        
        raise NotImplementedError()
        raise MultiThreadErrorInterface()