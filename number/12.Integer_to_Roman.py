def intToRoman_1(num: int) -> str:
    m = {
        1: "I",
        5: "V",    4: "IV",
        10: "X",   9: "IX",
        50: "L",   40: "XL",
        100: "C",  90: "XC",
        500: "D",  400: "CD",
        1000: "M", 900: "CM",
    }
    r = ''
    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        while n <= num:
            r += m[n]
            num-=n
    return r

def intToRoman_2(num: int) -> str:
    M=["","M","MM","MMM"]
    C=["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
    X=["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
    I=["","I","II","III","IV","V","VI","VII","VIII","IX"]
    return M[num//1000]+C[num%1000//100]+X[num%1000%100//10]+I[num%1000%100%10]
        
        
print("Input: 3")
print("Output: ", intToRoman_1(3))
print("")
print("Input: 58")
print("Output: ", intToRoman_1(58))
print("")
print("Input: 1994")
print("Output: ", intToRoman_1(1994))
print("")

print("Input: 3")
print("Output: ", intToRoman_2(3))
print("")
print("Input: 58")
print("Output: ", intToRoman_2(58))
print("")
print("Input: 1994")
print("Output: ", intToRoman_2(1994))
print("")