# Example 1:

# Input: 
n1 = 16
# Output: true
# Example 2:

# Input: 
n2 = 5
# Output: false
# Example 3:

# Input: 
n3 = 1
# Output: true

def isPowerOfFour1(n: int) -> bool:
    x = 1
    while x < n:
        x *= 4
    return x == n

from math import log, log2

def isPowerOfFour2(n: int) -> bool:
    return n > 0 and log2(n) % 2 == 0

def isPowerOfFour3(n: int) -> bool:
    return n > 0 and  (4 ** round(log(n, 4)) == n)

##  reursion
def isPowerOfFour4(n: int) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return isPowerOfFour4(n//4)
    return False

def isPowerOfFour5(n: int) -> bool:
        if n == 0:
            return False
        while n % 4 == 0:
            n //= 4
        return True if n == 1 else False


def isPowerOfFour6(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0 and n % 3 == 1
        



print(isPowerOfFour1(n1))
print(isPowerOfFour1(n2))
print(isPowerOfFour1(n3))

print(isPowerOfFour2(n1))
print(isPowerOfFour2(n2))
print(isPowerOfFour2(n3))

print(isPowerOfFour3(n1))
print(isPowerOfFour3(n2))
print(isPowerOfFour3(n3))

print(isPowerOfFour4(n1))
print(isPowerOfFour4(n2))
print(isPowerOfFour4(n3))

print(isPowerOfFour5(n1))
print(isPowerOfFour5(n2))
print(isPowerOfFour5(n3))

print(isPowerOfFour6(n1))
print(isPowerOfFour6(n2))
print(isPowerOfFour6(n3))
