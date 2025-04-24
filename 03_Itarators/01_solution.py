nums=[1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
#count positive and negative numbers
positive_count = 0
negative_count = 0 

for i in nums:
    if i > 0:
        positive_count += 1
    elif i < 0:
        negative_count += 1

print(f"Count of positive numbers: {positive_count}")
print(f"Count of negative numbers: {negative_count}")