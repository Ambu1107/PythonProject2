#List functions
data=list(map(int,input("Enter the number: ").split()))
print(f"The length of list is {len(data)}")
print(f"The largest element is {max(data)}")
print(f"The smallest element is {min(data)}")
print(f"The sorted list: {sorted(data)}")
print(f"The sum of all elements is {sum(data)}")

data.sort(reverse=True)
print(f"The sorted list in descending : {data}")