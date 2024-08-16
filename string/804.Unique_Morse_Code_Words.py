# Example 1:

# Input: 
words1 = ["gin","zen","gig","msg"]
# Output: 2
# Explanation: The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# There are 2 different transformations: "--...-." and "--...--.".
# Example 2:

# Input: 
words2 = ["a"]
# Output: 1
def uniqueMorseRepresentations(words) -> int:
    code = [
        ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
        "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
        "...-",".--","-..-","-.--","--.."
    ]
    store = []
    for word in words:
        wordCoder = ""
        for letter in word:
            wordCoder += code[ord(letter)-97]
        if wordCoder not in store:
            store.append(wordCoder)
    return len(store)

print(uniqueMorseRepresentations(words1))
print(uniqueMorseRepresentations(words2))

def uniqueMorseRepresentations2(words) -> int:
    code = [
        ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
        "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
        "...-",".--","-..-","-.--","--.."
    ]
    store = set()
    for word in words:
        wordCoder = ""
        for letter in word:
            wordCoder += code[ord(letter)-97]
        store.add(wordCoder)
    return len(store)

print(uniqueMorseRepresentations2(words1))
print(uniqueMorseRepresentations2(words2))