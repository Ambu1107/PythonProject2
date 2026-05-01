#On the basis of percentage print grades
n=int(input("Enter the number : "))
if n>=0 and n<=100:
    if n>=90:
        grade='A'
    elif n>=80:
        grade='B'
    elif n>=70:
        grade='C'
    elif n>=60:
        grade='D'
    else:
        grade='Fail'
    print(f"The grade of {n} is {grade}")
else:
    print("Enter valid percentage")