#3.2.6 Numpy: Searching, Sorting, Counting, Broadcasting
import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
indices=np.where(array1==search_value)
print(indices[0])
# Count occurrences in array1
index1=np.count_nonzero(array1==count_value)
print(index1)
# Broadcasting addition
print(array1+broadcast_value)
# Sort the first array
sorted=np.sort(array1)
print(sorted)