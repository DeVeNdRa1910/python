marks = int(input("Provide me your marks: "))

if marks > 100 or marks < 0:
    print("Invalid marks")
    exit()

grade = "A" if marks >= 90 else "B" if marks >= 80 else "C" if marks >= 70 else "D" if marks >= 60 else "F"

if marks >= 90:
    grade = "A"
    if marks >= 80:
        grade = "B"
        if marks >= 70:
            grade = "C"
            if marks >= 60:
                grade = "D"
            else :
                grade = "F"


#method 2

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else :
    grade = "F"

print(f"Your grade is {grade}")