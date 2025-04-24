n = int(input("Enter a number: "))

ans = 1

while n > 0:
    ans *= n
    n -= 1

print(ans)