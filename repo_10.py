#From a list of numbers separate even and odd numbers count them, find their sums
data=list(map(int,input("Enter the elements of the list: ").split()))
even=[]
odd=[]
Even=0
Odd=0
for i in data:
    if i%2==0:
        even.append(i)
        Even+=1
    else:
        odd.append(i)
        Odd+=1
print(f"For the given list of numbers: \nEven numbers are {even} and its count is {Even}")
print(f"Odd numbers are {odd} and its count is {Odd}")