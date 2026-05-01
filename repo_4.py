#Print how many and which vowels are present in a given string
vowels=['a','e','i','o','u','A','E','I','O','U']
char=input("Enter a string: ")
count=0
for i in range(len(char)):
    if char[i] in vowels:
        print(char[i],end=" ")
        count+=1
print()
print(f"In the given string {char}, There are {count} vowels.")