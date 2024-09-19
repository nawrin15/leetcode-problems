# Example 1:

# Input: 
words1 = ["one.two.three","four.five","six"]
separator1 = "."
# Output: ["one","two","three","four","five","six"]
# Explanation: In this example we split as follows:

# "one.two.three" splits into "one", "two", "three"
# "four.five" splits into "four", "five"
# "six" splits into "six" 

# Hence, the resulting array is ["one","two","three","four","five","six"].
# Example 2:

# Input: 
words2 = ["$easy$","$problem$"]
separator2 = "$"
# Output: ["easy","problem"]
# Explanation: In this example we split as follows: 

# "$easy$" splits into "easy" (excluding empty strings)
# "$problem$" splits into "problem" (excluding empty strings)

# Hence, the resulting array is ["easy","problem"].
# Example 3:

# Input: 
words3 = ["|||"]
separator3 = "|"
# Output: []
# Explanation: In this example the resulting split of "|||" will contain only empty strings, 
# so we return an empty array []. 

def splitWordsBySeparator(words, separator: str):
    res = []
    for word in words:
        ws = ''
        for letter in word:
            if letter == separator:
                if ws:
                    res.append(ws)
                    ws = ''
            else:
                ws += letter
        if ws:
            res.append(ws)
    return res
        

print(splitWordsBySeparator(words1, separator1))
print(splitWordsBySeparator(words2, separator2))


def splitWordsBySeparator1(words, separator: str):
    res = []
    for word in words:
        for j in word.split(separator):
            if j:
                res.append(j)
    return res
        

print(splitWordsBySeparator1(words1, separator1))
print(splitWordsBySeparator1(words2, separator2))