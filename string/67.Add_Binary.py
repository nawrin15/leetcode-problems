a1 = "11"
b1 = "1"
# Output: "100"

a2 = "1010"
b2 = "1011"
# Output: "10101"
    
def addBinary(a: str, b: str) -> str:
    carry = 0
    res = []
    a = a[::-1]
    b = b[::-1]
    for i in range(max(len(a), len(b))):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0
        print(digit_a, digit_b)
        total = digit_a + digit_b + carry  
        res.append(str(total % 2))
        carry = total // 2
    if carry == 1:
        res.append(str(carry))
    return "".join(res[::-1])
    

print(addBinary(a1, b1))
print(addBinary(a2, b2))