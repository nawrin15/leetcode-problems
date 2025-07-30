Example 1:

Input: 
s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: 
s2 = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


def findRepeatedDnaSequences(s):
    """
    :type s: str
    :rtype: List[str]
    """
    dic = {}
    res = []
    for i in range(len(s)-9):
        window = s[i:i+9]
        print(window)

print(findRepeatedDnaSequences(s1))
print(findRepeatedDnaSequences(s2))