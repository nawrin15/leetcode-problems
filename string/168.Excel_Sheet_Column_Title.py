# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
 

# Example 1:

# Input: 
columnNumber1 = 1
# Output: "A"
# Example 2:

# Input: 
columnNumber2 = 28
# Output: "AB"
# Example 3:

# Input: 
columnNumber3 = 701
# Output: "ZY"


def convertToTitle(columnNumber: int) -> str:
    res = []
    while columnNumber > 0:
        columnNumber -= 1
        res.append(chr((columnNumber % 26) + 65))
        columnNumber //= 26
    return "".join(res[::-1])


print(convertToTitle(columnNumber1))
print(convertToTitle(columnNumber2))
print(convertToTitle(columnNumber3))