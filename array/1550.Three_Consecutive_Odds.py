# Example 1:

# Input: 
arr1 = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
# Example 2:

# Input: 
arr2 = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.

def threeConsecutiveOdds(arr) -> bool:
    count = 0
    for num in arr:
        if num % 2 == 0:
            count = 0
        else:
            count += 1
        if count == 3:
            return True
    return False

print(threeConsecutiveOdds(arr1))
print(threeConsecutiveOdds(arr2))

def threeConsecutiveOdds1(arr) -> bool:
    for i in range(len(arr) - 2):
        if((arr[i] % 2 != 0) and (arr[i+1] % 2 != 0) and (arr[i+2] % 2 != 0)):
            return True
    return False

print(threeConsecutiveOdds1(arr1))
print(threeConsecutiveOdds1(arr2))