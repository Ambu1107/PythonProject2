#Find second largest number in a list
data=list(map(int,input("Enter the elements of the list: ").split()))

'''largest=float('-inf')
second=float('-inf')
for i in range(0,len(data)):
    if data[i]>largest:
        second=largest
        largest=data[i]
    elif data[i]>second:
        second=data[i]
print(f"The second largest element is {second}\nThe largest element is {largest}")'''

#Second way
#By using heapq we can find nth largest element in a list
'''import heapq
second2=heapq.nlargest(2,data)[1]
#heapq gives list of largest and nth largest elements (here largest and second largest)
print(f"The second largest element is {second2}")'''