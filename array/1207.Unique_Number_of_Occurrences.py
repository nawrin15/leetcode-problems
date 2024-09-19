# Example 1:

# Input: 
arr1 = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:

# Input: 
arr2 = [1,2]
# Output: false
# Example 3:

# Input: 
arr3 = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true

from collections import Counter

def uniqueOccurrences(arr) -> bool:
    count = Counter(arr)
    counter_set = set()
    for i in count:
        if count[i] not in counter_set:
            counter_set.add(count[i])
        else:
            return False
    return True

print(uniqueOccurrences(arr1))
print(uniqueOccurrences(arr2))
print(uniqueOccurrences(arr3))

def uniqueOccurrences1(arr) -> bool:
    count = list(Counter(arr).values())
    return len(count) == len(set(count))

print(uniqueOccurrences1(arr1))
print(uniqueOccurrences1(arr2))
print(uniqueOccurrences1(arr3))