import os
import psutil


def get_process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss


def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory()
        result = func(*args, **kwargs)
        mem_after = get_process_memory()
        print("{}: memory before: {:,}, after: {:,}, consumed: {:,};".format(
            func.__name__, mem_before, mem_after, mem_after - mem_before
        ))
        return result
    return wrapper


