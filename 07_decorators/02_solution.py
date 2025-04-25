# Create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(func):
    def wrapper(*args, **kwargs):
        funcName = func.__name__
        argsList = ', '.join(str(args) for arg in args)
        kwargsList = ', '.join(f"{k}: {v}" for k, v in kwargs.items())
        print(f"Function name: {funcName}")
        print(f"Arguments: {argsList}")
        print(f"keyword arguments: {kwargsList}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greeting="Namaste"):
    print(f"{greeting}, {name}!")

greet("Jahnvi", greeting="LOL")