import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' ran in {end_time - start_time} seconds")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)
    print(f"Function executed with argument: {n}")
    return

example_function(5)