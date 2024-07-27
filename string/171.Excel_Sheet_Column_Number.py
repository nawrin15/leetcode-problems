# Example 1:

# Input: 
columnTitle1 = "A"
# Output: 1
# Example 2:

# Input: 
columnTitle2 = "AB"
# Output: 28
# Example 3:

# Input: 
columnTitle3 = "ZY"
# Output: 701



def titleToNumber(columnTitle: str) -> int:
    result = 0
    n = len(columnTitle)
    for i in range(len(columnTitle)):
        charVal = ord(columnTitle[i]) - 64  
        result += (charVal * pow(26, n - i - 1))
    return result


def titleToNumber1(columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64
            ans += digit * 26**pos
            pos += 1
            
        return ans


print(titleToNumber(columnTitle1))
print(titleToNumber(columnTitle2))
print(titleToNumber(columnTitle3))

print(titleToNumber1(columnTitle1))
print(titleToNumber1(columnTitle2))
print(titleToNumber1(columnTitle3))
