def reverseVowels(s: str) -> str:
    sList = list(s)
    start = 0
    end = len(sList) - 1
    vowels = 'aeiouAEIOU'
    while start < end:
        if sList[start] in vowels and sList[end] in vowels:
            temp = sList[start]
            sList[start] = sList[end]
            sList[end] = temp
            end -= 1
            start += 1
        elif sList[start] not in vowels:
            start += 1
        elif sList[end] not in vowels:
            end -= 1
    return "".join(sList)

print(reverseVowels('leetcode'))