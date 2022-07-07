from sys import path
path.append('../')

from qtbsoundtable.source.multi_thread.multi_thread_error import MultiThreadError

def test_answer():
    # Error class
    multi_thread_error = MultiThreadError("Multi Thread Error")
    try:
        raise multi_thread_error
    except MultiThreadError:
        assert True