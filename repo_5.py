#Print number of digits in a number and reverse of the number
n=int(input("Enter a number: "))
digits=0
for i in str(n):
    digits+=1
n=str(n)
reverse=int(n[::-1])
print(f"For the given number {n}:\nThe number of digits are {digits}\n"
     f"The reverse of given number is {reverse}")