# Input: 
key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"
# Output: "this is a secret"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog"
# Input: 
key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
# Output: "the five boxing wizards jump quickly"
# Explanation: The diagram above shows the substitution table.
# It is obtained by taking the first appearance of each letter in "eljuxhpwnyrdgtqkviszcfmabo".


def decodeMessage(key: str, message: str) -> str:
    p = 97
    coder = {}
    for i in range(len(key)):
        if key[i] != " " and key[i] not in coder:
            coder[key[i]] = chr(p)
            p += 1
    res = "" 
    for char in message:
        if char == " ":
            res += char
        else:
            res += coder[char]
    return res

print(decodeMessage(key1, message1))
print(decodeMessage(key2, message2))