# Example 1:

# Input: 
date1 = "2080-02-29"

# Output: "100000100000-10-11101"

# Explanation:

# 100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

# Example 2:

# Input: 
date2 = "1900-01-01"

# Output: "11101101100-1-1"

# Explanation:

# 11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.

def convertDateToBinary(date: str) -> str:
    y, m, d = map(int, date.split('-'))
    def convertBinary(n):
        binary = []
        while n > 0:
            binary.append(n%2)
            n //= 2
    return 

print(convertDateToBinary(date1))
print(convertDateToBinary(date2))