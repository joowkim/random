import time

__author__ = "jkkim"


def printer(func):
    def wrapper(*args, **kwargs):
        print(func(*args, **kwargs))

    return wrapper


def check_the_elapsed_time(original_function):  # 1
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(
            'THe {} takes {} !'.format(original_function.__name__, t2)
        )
        return result

    return wrapper


def benchmark(func):
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print("\t%s" % func.__name__, time.clock() - t)
        return res
    return wrapper
