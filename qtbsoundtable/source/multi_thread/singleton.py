from .multi_thread_error import MultiThreadError
from .multi_thread import MultiThread

MultiThreadClass = MultiThread(error_class=MultiThreadError)