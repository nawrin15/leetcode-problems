# Example 1:

# Input: 
s1 = "string"
# Output: "rtsng"
# Explanation: 
# After typing first character, the text on the screen is "s".
# After the second character, the text is "st". 
# After the third character, the text is "str".
# Since the fourth character is an 'i', the text gets reversed and becomes "rts".
# After the fifth character, the text is "rtsn". 
# After the sixth character, the text is "rtsng". 
# Therefore, we return "rtsng".
# Example 2:

# Input: 
s2 = "poiinter"
# Output: "ponter"
# Explanation: 
# After the first character, the text on the screen is "p".
# After the second character, the text is "po". 
# Since the third character you type is an 'i', the text gets reversed and becomes "op". 
# Since the fourth character you type is an 'i', the text gets reversed and becomes "po".
# After the fifth character, the text is "pon".
# After the sixth character, the text is "pont". 
# After the seventh character, the text is "ponte". 
# After the eighth character, the text is "ponter". 
# Therefore, we return "ponter".

def finalString(s: str) -> str:
    res = ""
    # if s.count('i') == 0:
    #         return s
    for letter in s:
        if letter == "i":
            res = res[::-1]
        else:
            res += letter
    return res

print(finalString(s1))
print(finalString(s2))

def finalString2(s: str) -> str:
    return ''.join([res[::-1] if letter == 'i' else res + letter for res, letter in zip([''] * (len(s) + 1), s)])

print(finalString2(s1))
print(finalString2(s2))

from functools import reduce

def finalString3(s: str) -> str:
    return reduce(lambda res, letter: res[::-1] if letter == 'i' else res + letter, s, "")

print(finalString3(s1))
print(finalString3(s2))

def finalString4(s: str) -> str:
    return (lambda res: [(res:=res[::-1] if letter == 'i' else res + letter) for letter in s][-1])("")

print(finalString4(s1))
print(finalString4(s2))