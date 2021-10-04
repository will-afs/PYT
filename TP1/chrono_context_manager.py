from time import perf_counter
from functools import wraps
from contextlib import contextmanager

class Chrono(object):
    """
    Meters the time taken between __enter__() and __exit__() methods.
    Typically used as a context manager as : 

    chrono = Chrono()
    with chrono:
        sleep(3)
    print(chrono.elapsed)
    
    """
    def __enter__(self):
        self.__start_time = perf_counter()

    def __exit__(self, type, value, traceback):
        end_time = perf_counter()
        self.elapsed = end_time - self.__start_time

def time_exc_measure(func):
    @wraps(func)
    def wrapper(*args):
        timer = Chrono()
        with timer:
            func(*args)
        print('Time elapsed for executing ' + func.__name__ + ' : ' + str(timer.elapsed) + ' seconds.')
    return wrapper
    
@time_exc_measure
def hello_world():
    """Dummy Hello World function printing 'Hello World'."""
    print('Hello')

# hello_world=time_exc_measure(hello_world)
# print(hello_world())


if __name__ == "__main__":
    hello_world()
    print(hello_world.__doc__)
    print(hello_world.__name__)