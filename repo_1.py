#Check whether the number is prime or composite
n=int(input("Enter a number: "))
if n>0:
    if n==1:
        print("1 is neither prime nor composite")
    else:
        for i in range(2,n):
            if n%i==0:
                print(f"{n} is composite number!!")
                break
        else:
            print(f"{n} is prime number!!")
elif n==0:
    print("You have entered 0, please enter a number greater than 0")
else:
    print("Your input is negative, Please insert positive number")