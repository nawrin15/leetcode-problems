######### 151. Reverse Words in a String

s = "  hello world "
sList = s.split()
i = len(sList) - 1
rev_str = ""
while i >= 0:
    rev_str += (" " + sList[i])
    i -= 1

print(str.strip(rev_str))

    