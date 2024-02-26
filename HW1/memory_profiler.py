import functools
import tracemalloc


def get_memory():
    mem = tracemalloc.get_tracemalloc_memory()
    return round(mem / 1024, 2)


def profile(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        mem_before = get_memory()
        result = func(*args, **kwargs)
        mem_after = get_memory()
        print("{}: memory before: {:,} KB, after: {:,} KB, consumed: {:,} KB;".format(
            func.__name__, mem_before, mem_after, mem_after - mem_before
        ))
        return result
    return wrapper


