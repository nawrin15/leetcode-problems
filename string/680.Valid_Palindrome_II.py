s1 = "aba"
# Output: true

s2 = "abca"
# Output: true

s3 = "abc"
# Output: false

def validPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            skipl, skipr = s[l+1:r+1], s[l:r]
            print("left", skipl, skipl[::-1])
            print("right", skipr, skipr[::-1])
            return (skipl == skipl[::-1]) or (skipr == skipr[::-1])
        l, r = l + 1, r - 1
    return True

print(validPalindrome(s1))
print(validPalindrome(s2))
print(validPalindrome(s3))