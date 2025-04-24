num = int(input("Enter a number; "))

for i in range(2, num-1):
    if num % i == 0:
        print(f"Given number is not prime")
        exit()
    
print(f"Given number is prime")