# Example 1:

# Input: 
digits1 = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: 
digits2 = ""
# Output: []
# Example 3:

# Input: 
digits3 = "2"
# Output: ["a","b","c"]

def letterCombinations(digits: str):
    if not digits:
        return ""
    phone = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    res = []
    def dfs(combo, nxt):
        if not nxt:
            res.append(combo)
            return
        for letter in phone[nxt[0]]:
            dfs(combo + letter, nxt[1:])
    
    dfs("", digits)
    return res

print(letterCombinations(digits1))
print(letterCombinations(digits2))
print(letterCombinations(digits3))

def letterCombinations(digits: str):
    phone = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    res = []
    def dfs(combo, iter):
        if len(digits) == iter:
            if combo:
                res.append(combo)
            return
        for letter in phone[digits[iter]]:
            dfs(combo + letter, iter + 1)
    
    dfs("", 0)
    return res

print(letterCombinations(digits1))
print(letterCombinations(digits2))
print(letterCombinations(digits3))



