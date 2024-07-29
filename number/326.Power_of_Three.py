
# Example 1:

# Input: 
n1 = 27
# Output: true
# Explanation: 27 = 33
# Example 2:

# Input: 
n2 = 0
# Output: false
# Explanation: There is no x where 3x = 0.
# Example 3:

# Input: 
n3 = -1
# Output: false
# Explanation: There is no x where 3x = (-1).

def isPowerOfThree1(n: int) -> bool:
    x = 1
    while x < n:
        x *= 3
    return x == n

from math import log

def isPowerOfThree2(n: int) -> bool:
    return n > 0 and ((3 ** 19) % n == 0)

def isPowerOfThree3(n: int) -> bool:
    return n > 0 and  (3 ** round(log(n, 3)) == n)

##  reursion
def isPowerOfThree4(n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 3 == 0:
        return isPowerOfThree4(n//3)
    return False

def isPowerOfThree5(n: int) -> bool:
        if n == 0:
            return False
        while n % 3 == 0:
            n //= 3
        return True if n == 1 else False

print(isPowerOfThree1(n1))
print(isPowerOfThree1(n2))
print(isPowerOfThree1(n3))

print(isPowerOfThree2(n1))
print(isPowerOfThree2(n2))
print(isPowerOfThree2(n3))

print(isPowerOfThree3(n1))
print(isPowerOfThree3(n2))
print(isPowerOfThree3(n3))

print(isPowerOfThree4(n1))
print(isPowerOfThree4(n2))
print(isPowerOfThree4(n3))

print(isPowerOfThree5(n1))
print(isPowerOfThree5(n2))
print(isPowerOfThree5(n3))