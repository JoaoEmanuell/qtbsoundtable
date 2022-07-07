from sys import path
from time import sleep
path.append('../')

from qtbsoundtable.source import Factory
from qtbsoundtable.source.multi_thread.multi_thread_error import MultiThreadError
from qtbsoundtable.source.multi_thread import MultiThreadInterface

def test_answer():
    # Error class
    multi_thread_error = MultiThreadError("Multi Thread Error")
    try:
        raise multi_thread_error
    except MultiThreadError:
        assert True

    # Multi Thread

    fac = Factory()

    multi_thread : MultiThreadInterface \
        = fac.get_representative(MultiThreadInterface)

    assert isinstance(multi_thread, MultiThreadInterface)

    thread_id = multi_thread.create_thread(target=__test_thread, args=(5,))

    assert type(thread_id) == int

    sleep(0.5)

    # Restart

    multi_thread.start_thread(thread_id)

    # Stop

    multi_thread.stop_thread(thread_id)

    # Is alive

    assert multi_thread.is_alive(thread_id) == True

    # Delete

    multi_thread.delete_thread(thread_id)

    # Limit

    try:
        for _ in range(0, 15):
            id = multi_thread.create_thread(target=__test_thread, args=(10,))
            multi_thread.stop_thread(id)
    except MultiThreadError:
        pass

def __test_thread(max: int):
    for i in range(max):
        sleep(0.1)
        print(i)

if __name__ == '__main__':
    test_answer()