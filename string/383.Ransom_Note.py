# Example 1:

# Input: 
ransomNote1 = "a"
magazine1 = "b"
# Output: false


# Example 2:

# Input:
ransomNote2 = "aa"
magazine2 = "ab"
# Output: false
# Example 3:

# Input: 
ransomNote3 = "aa"
magazine3 = "aab"
# Output: true

from collections import Counter, defaultdict

def canConstruct(ransomNote: str, magazine: str) -> bool:
    print("Using Counter")
    print("=============")
    r = Counter(ransomNote)
    m = Counter(magazine)
    for i in r:
        if m[i] < r[i]:
            return False
    return True

def canConstruct1(ransomNote: str, magazine: str) -> bool:
    print("Using Dict")
    print("=============")
    counter = defaultdict(int)
    for i in magazine:
        counter[i] += 1

    for i in ransomNote:
        counter[i] -= 1
        if counter[i] < 0:
            return False
    return True

   

print(canConstruct(ransomNote1, magazine1))
print(canConstruct(ransomNote2, magazine2))
print(canConstruct(ransomNote3, magazine3))
print("\n")

print(canConstruct1(ransomNote1, magazine1))
print(canConstruct1(ransomNote2, magazine2))
print(canConstruct1(ransomNote3, magazine3))