# Example 1:

# Input: 
s1 = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
# Example 2:

# Input: 
s2 = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

def checkRecord(s: str) -> bool:
    a = 0
    l = 0
    for i in range(len(s)):
        if s[i] == "A":
            a += 1
        elif s[i] == "L":
            if i > 0 and s[i-1] == 'L':
                l += 1
            else:
                l = 1
        if l >= 3 or a >= 2:
            return False
    return True

print(checkRecord(s1))
print(checkRecord(s2))

def checkRecord(s: str) -> bool:
    return s.count('A') < 2 and 'LLL' not in s

print(checkRecord(s1))
print(checkRecord(s2))