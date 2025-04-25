def sum_all(*args):
    print(args)
    for i in args:
        print(i * 5)
    return sum(args)

# print(sum_all(1,2,3))
print(sum_all(1,2,3,4,5,6))
# print(sum_all(1,2,3,5,6,7,8,9))