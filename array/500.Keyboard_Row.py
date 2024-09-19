# Example 1:

# Input: 
words1 = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:

# Input: 
words2 = ["omk"]
# Output: []
# Example 3:

# Input: 
words3 = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]

def findWords(words):
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    res = []
    for word in words:
        s = str.lower(word)
        index = -1
        for i in range(3):
            if s[0] in keyboard[i]:
                index = i
            n = len(word)
        for i in range(len(word)):
            if s[i] not in keyboard[index]:
                break
            if i == n - 1:
                res.append(word)
    return res

print(findWords(words1))
print(findWords(words2))
print(findWords(words3))

def findWords1(words):
    row = {}
    for i in "qwertyuiop":
        row[i] = 0
    for i in "asdfghjkl":
        row[i] = 1
    for i in "zxcvbnm":
        row[i] = 2

    def is_single_row(word): 
        s = str.lower(word)
        key = row[s[0]]
        for i in range(len(word)):
            if row[s[i]] != key:
                return False
        return True
    
    return [word for word in words if is_single_row(word)]

print(findWords1(words1))
print(findWords1(words2))
print(findWords1(words3))

def findWords2(words):
    keyboard = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
    res = []
    for word in words:
        for row in keyboard:
            if set(str.lower(word)) <= row:
            # if set(str.lower(word)).issubset(row):
                res.append(word)
    return res
    

print(findWords2(words1))
print(findWords2(words2))
print(findWords2(words3))
