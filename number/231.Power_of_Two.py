# Example 1:

# Input: 
n1 = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: 
n2 = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: 
n3 = 3
# Output: false

def isPowerOfTwo1(n: int) -> bool:
    x = 1
    while x < n:
        x *= 2
    return x == n

#complexity logn
def isPowerOfTwo2(n: int) -> bool:
    return n > 0 and (n & (n - 1) == 0)


def isPowerOfTwo3(n: int) -> bool:
    return n > 0 and ((2 ** 30) % n == 0)

def isPowerOfTwo4(n: int) -> bool:
    return n > 0 and ((1 << 30) % n == 0)


print(isPowerOfTwo1(n1))
print(isPowerOfTwo1(n2))
print(isPowerOfTwo1(n3))


print(isPowerOfTwo2(n1))
print(isPowerOfTwo2(n2))
print(isPowerOfTwo2(n3))


print(isPowerOfTwo3(n1))
print(isPowerOfTwo3(n2))
print(isPowerOfTwo3(n3))

print(isPowerOfTwo4(n1))
print(isPowerOfTwo4(n2))
print(isPowerOfTwo4(n3))

print(1 << 2)
print((2 ** 30) % 5)