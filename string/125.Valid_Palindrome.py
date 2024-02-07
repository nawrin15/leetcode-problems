s1 = "A man, a plan, a canal: Panama"
# Output: true

s2 = "race a car"
# Output: false

s3 = " "
# Output: true

def isPalindrome1(s: str):
    if not s: return True
    filter_str = ""
    for letter in s:
        if letter.isalnum():
            filter_str += letter.lower()
    return filter_str == filter_str[::-1]



print(isPalindrome1(s1))
print(isPalindrome1(s2))
print(isPalindrome1(s3))

def isAlphaNum(char):
    return ord('A') <= ord(char) <= ord('Z') or \
        ord('a') <= ord(char) <= ord('z') or \
        ord('0') <= ord(char) <= ord('9')
        

def isPalindrome2(s: str):
    l = 0
    r = len(s) - 1 
    while l < r:
        if not isAlphaNum(s[l]):
            l += 1
        elif not isAlphaNum(s[r]):
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
    return True
    
print(isPalindrome2(s1))
print(isPalindrome2(s2))
print(isPalindrome2(s3))

def isPalindrome3(s: str):
    l, r = 0, len(s) - 1 
    while l < r:
        while l < r and not isAlphaNum(s[l]):
            l += 1
        while r > 1 and not isAlphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True
    
print(isPalindrome3(s1))
print(isPalindrome3(s2))
print(isPalindrome3(s3))