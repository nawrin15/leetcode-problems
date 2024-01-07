

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
prev = None
count = 1

for i in range(len(chars)-1,-1,-1):
    curr = chars[i]
    if i != 0 and chars[i-1] == chars[i]:
        chars.pop(i)
        count += 1
    else:
        if count > 1:
            for j in [*str(count)][::-1]:
                chars.insert(i + 1, j)
        count = 1


print(chars)
        