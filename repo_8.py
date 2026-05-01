#Print Pattern
n=int(input("Enter the number: "))
for i in range(1,n+2):
    for j in range(1,i):
        print(j,end=" ")
    print()