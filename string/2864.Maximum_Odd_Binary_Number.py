# Example 1:

# Input: 
s1 = "010"
# Output: "001"
# Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
# Example 2:

# Input: 
s2 = "0101"
# Output: "1001"
# Explanation: One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

def maximumOddBinaryNumber(s: str) -> str:
    count = 0
    for i in s:
        if i == "1":
            count += 1
    return "1" * (count-1) + "0" * (len(s) - count) + "1" 

print(maximumOddBinaryNumber(s1))
print(maximumOddBinaryNumber(s2))


def maximumOddBinaryNumber2(s: str) -> str:
    one_count = s.count("1")
    zero_count = len(s) - one_count
    return "1" * (one_count - 1) + "0" * zero_count + "1" 

print(maximumOddBinaryNumber2(s1))
print(maximumOddBinaryNumber2(s2))

def maximumOddBinaryNumber3(s: str) -> str:
    s = sorted(s, reverse=True)
    for i in range(len(s)):
        if s[i] == "0":
            s[i - 1], s[len(s) - 1] = s[len(s) - 1], s[i - 1]
            break
    return "".join(s)

print(maximumOddBinaryNumber3(s1))
print(maximumOddBinaryNumber3(s2))