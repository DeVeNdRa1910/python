today = input("Today is: ")
age = int(input("Provide me your age: "))

if today != "Wednesday":
    if age < 18:
        print("Ticket price is $8")
    else:
        print("Ticket price is $12")
else:
    if age < 18:
        print("Ticket price is $6")
    else:
        print("Ticket price is $10")


#method 2
price = 12 if age > 18 else 8

if today == "Wednesday":
    price = price - 2

print(f"Ticket price is ${price}")