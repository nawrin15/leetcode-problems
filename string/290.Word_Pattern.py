pattern1 = "abba"
s1 = "dog cat cat dog"
# Output: true

pattern2 = "abba"
s2 = "dog cat cat fish"
# Output: false

pattern3 = "aaaa"
s3 = "dog cat cat dog"
# Output: false
pattern4 = "aaa"
s4 = "aa aa aa aa"


def wordPattern1(pattern: str, s: str):
    word_2_char = {}
    char_2_word = {}
    s_list = s.split(" ")
    if len(pattern) != len(s_list): return False
    for i in range(len(pattern)):
        if (pattern[i] in char_2_word and char_2_word[pattern[i]] != s_list[i]) or \
            (s_list[i] in word_2_char and word_2_char[s_list[i]] != pattern[i]): 
            return False
        char_2_word[pattern[i]] = s_list[i]
        word_2_char[s_list[i]] = pattern[i]    
    return True


def wordPattern2(pattern, str):
    s = pattern
    t = str.split()
    return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

def wordPattern3(pattern, s):
    f = lambda s: map({}.setdefault, s, range(len(s)))
    return list(f(pattern)) == list(f(s.split()))

def wordPattern4(pattern, str):
    s = pattern
    t = str.split()
    return list(map(s.find, s)) == list(map(t.index, t))

print(wordPattern1(pattern1, s1))
print(wordPattern1(pattern2, s2))
print(wordPattern1(pattern3, s3))
print(wordPattern1(pattern4, s4))

print(wordPattern2(pattern1, s1))
print(wordPattern2(pattern2, s2))
print(wordPattern2(pattern3, s3))
print(wordPattern2(pattern4, s4))

print(wordPattern3(pattern1, s1))
print(wordPattern3(pattern2, s2))
print(wordPattern3(pattern3, s3))
print(wordPattern3(pattern4, s4))

print(wordPattern4(pattern1, s1))
print(wordPattern4(pattern2, s2))
print(wordPattern4(pattern3, s3))
print(wordPattern4(pattern4, s4))