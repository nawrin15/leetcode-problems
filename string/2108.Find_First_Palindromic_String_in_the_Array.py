# Example 1:

# Input: 
words1 = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
# Example 2:

# Input: 
words2 = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
# Example 3:

# Input: 
words3 = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.
words4 = ["xngla","e","itrn","y","s","pfp","rfd"]
words5 = ["njzejpscyerhspkqnllhlgoijvtuzwxmesdauvs", "bxyttlorydrofawwqblxnameywdtmlccvlvcclmtdwyemanxlbqwwafordyrolttyxb"]

def firstPalindrome(words) -> str:
    for j in range(len(words)):
        word = words[j]
        n = len(word)
        if n == 1:
            return word
        for i in range(n//2):
            if word[i] != word[n-i-1]:
                break
            if i == (n // 2)-1:
                return word
    return ""

print(firstPalindrome(words1))
print(firstPalindrome(words2))
print(firstPalindrome(words3))
print(firstPalindrome(words4))
print(firstPalindrome(words5))

def firstPalindrome2(words) -> str:
        for i in words:
            if i==i[::-1]:
                return i
        return ""


print(firstPalindrome2(words1))
print(firstPalindrome2(words2))
print(firstPalindrome2(words3))
print(firstPalindrome2(words4))
print(firstPalindrome2(words5))

def firstPalindrome3(words) -> str:
        for word in words:
            if word[0::] == word[::-1]:
                return word
        return ''

print(firstPalindrome3(words1))
print(firstPalindrome3(words2))
print(firstPalindrome3(words3))
print(firstPalindrome3(words4))
print(firstPalindrome3(words5))