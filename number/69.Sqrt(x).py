# Example 1:

# Input: 
x1 = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: 
x2 = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


def mySqrt(x: int) -> int:
    sqrt = 1
    while sqrt * sqrt <= x:
        sqrt += 1
    return sqrt - 1

print(mySqrt(x1))
print(mySqrt(x2))

def mySqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x
    left, right = 0, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif (mid * mid) < x:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1 

print(mySqrt(x1))
print(mySqrt(x2))