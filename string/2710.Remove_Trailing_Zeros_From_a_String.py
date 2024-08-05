# Example 1:

# Input: 
num1 = "51230100"
# Output: "512301"
# Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".
# Example 2:

# Input: 
num2 = "123"
# Output: "123"
# Explanation: Integer "123" has no trailing zeros, we return integer "123".

def removeTrailingZeros1(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if num[i] != "0":
            return num[0:i+1]
    return num

print(removeTrailingZeros1(num1))
print(removeTrailingZeros1(num2))

def removeTrailingZeros2(num: str) -> str:
        n=num[::-1]
        p=int(n)
        a=str(p)
        a=a[::-1]
        return a


print(removeTrailingZeros2(num1))
print(removeTrailingZeros2(num2))

def removeTrailingZeros3(num: str) -> str:
    return num.rstrip('0')

print(removeTrailingZeros3(num1))
print(removeTrailingZeros3(num2))