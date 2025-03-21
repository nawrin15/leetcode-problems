# Example 1:

# Input: 
digits1 = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: 
digits2 = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: 
digits3 = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

def plusOne(digits):
    i = len(digits) - 1 
    while i > -1:
        if digits[i] == 9:
            digits[i] = 0
            i -= 1
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits

print(plusOne(digits1))
print(plusOne(digits2))
print(plusOne(digits3))