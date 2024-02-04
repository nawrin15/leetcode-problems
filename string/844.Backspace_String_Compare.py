s1 = "ab#c"
t1 = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

s2 = "ab##"
t2 = "c#d#"
# Output: true
# Explanation: Both s and t become "".

s3 = "a#c"
t3 = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

s4 = "a##c"
t4 = "#a#c"
# Output: True
s5 ="y#fo##f"
t5 ="y#f#o##f"
# Output: True


def backspaceCompare1(s, t):
    stack1=[]
    stack2=[]
    for l in s:
        if l == "#":
            if len(stack1) != 0:
                stack1.pop()
        else:
            stack1.append(l)
    for l in t:
        if l == "#":
            if len(stack2) != 0:
                stack2.pop()
        else:
            stack2.append(l)
    print(stack1, stack2)
    return stack1 == stack2
    
print(backspaceCompare1(s1, t1))
print(backspaceCompare1(s2, t2))
print(backspaceCompare1(s3, t3))
print(backspaceCompare1(s4, t4))
print(backspaceCompare1(s5, t5))