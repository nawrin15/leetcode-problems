# Example 1:

# Input: 
numa1 = "11"
numa2 = "123"
# Output: "134"
# Example 2:

# Input: 
numb1 = "456"
numb2 = "77"
# Output: "533"
# Example 3:

# Input: 
numc1 = "0"
numc2 = "0"
# Output: "0"

#Runtime Error
def addStrings(num1: str, num2: str) -> str:
    return str(int(num1) + int(num2))

print(addStrings(numa1, numa2))
print(addStrings(numb1, numb2))
print(addStrings(numc1, numc2))

def addStrings(num1: str, num2: str) -> str:
    res = []
    carry = 0
    num1 = num1[::-1]
    num2 = num2[::-1]
    for i in range(max(len(num1), len(num2))):
        digit1 = int(num1[i]) if i < len(num1) else 0
        digit2 = int(num2[i]) if i < len(num2) else 0
        total = digit1 + digit2 + carry
        res.append(str(total % 10))
        carry = total // 10
    if carry:
        res.append(str(carry))
    return "".join(res[::-1])


print(addStrings(numa1, numa2))
print(addStrings(numb1, numb2))
print(addStrings(numc1, numc2))

def addStrings(num1: str, num2: str) -> str:
    res = []
    carry = 0
    n = len(num1) - 1 
    m = len(num2) - 1
    while n >= 0 or m >= 0 or carry:
        digit1 = int(num1[n]) if n >= 0 else 0
        digit2 = int(num2[m]) if m >= 0 else 0
        total = digit1 + digit2 + carry
        res.append(str(total % 10))
        carry = total // 10
        n -= 1
        m -= 1
    return "".join(res[::-1])


print(addStrings(numa1, numa2))
print(addStrings(numb1, numb2))
print(addStrings(numc1, numc2))