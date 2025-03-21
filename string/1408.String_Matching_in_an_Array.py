# Example 1:

# Input:
words1 = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: 
words2 = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: 
words3 = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.
words4 = [
    "uexk","aeuexkf","wgxih","yuexk","gxea","yuexkm",
    "ypmfx","jjuexkmb","wqpri","aeuexkfpo","kqtnz",
    "pkqtnza","nrbb","hmypmfx","krqs","jjuexkmbyt",
    "zvru","ypmfxj"
]
#output : ["uexk","aeuexkf","yuexk","ypmfx","jjuexkmb","kqtnz"]
def stringMatching(words):
    sentence = " ".join(words)
    return [i for i in words if sentence.count(i) > 1]

print(stringMatching(words1))
print(stringMatching(words2))
print(stringMatching(words3))
print(stringMatching(words4))

def stringMatching(words):
    words = set(words)
    res = set()
    for i, value1 in enumerate(words):
        for j, value2 in enumerate(words):
            if i != j and value1 in value2:
                res.add(value1)
                break
    return list(res)

print(stringMatching(words1))
print(stringMatching(words2))
print(stringMatching(words3))
print(stringMatching(words4))
    
 