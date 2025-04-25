x=99
def func1():
    x = 100
    def func2():
        print("x: ", x)
    return func2

tempFun = func1()
tempFun()

# here we are defining a function (func2) inside another function (func1)

def base(x):
    def power(num):
        return x ** num
    return power

temp = base(2)
print(temp(1000))