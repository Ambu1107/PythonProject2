#Calculate the factorial
'''n=int(input("Enter the number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(f"{n}! = {fact}")'''

#Second way
#Using recursive function (We can calculate factorial also by defining the function)
'''def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
print(f"{n}! = {fact(n)}")'''
