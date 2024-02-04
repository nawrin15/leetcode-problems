strs1 = ["flower","flow","flight"]
#Output: "fl"

strs2 = ["dog","racecar","car"]
#Output: ""

def longestCommonPrefix(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += (strs[0][i])
    return res
        
print(longestCommonPrefix(strs1))
print(longestCommonPrefix(strs2))