x = 100

def func():
    x = 200
    print("x: ", x)

print("x: ", x)
# This function will print the value of x defined in the outer scope
func()
print("X: ", x)

def func2():
    y = 200
    print("y: ", y)

# print("y: ", y) # This will raise an error because y is not defined in this scope
func2()

p=199
def func3(s):
    q=p+s
    return q
# Here we are using variable p from the outer scope
print(func3(1))

# extream outer context is global context(direct inside of file)

a=100
def func4():
    global a
    a = 200
    print("a: ", a)

print("a: ", a)
func4()
print("a: ", a)


