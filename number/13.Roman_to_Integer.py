def romanToInt_1(s):
        """
        :type s: str
        :rtype: int
        """
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
       "M": 1000
        }
        n = len(s)
        res = 0
        for i in range(n):
            if i < n-1 and m[s[i]] < m[s[i+ 1]]:
                res -= m[s[i]]
            else:
                res += m[s[i]]
        return res

def romanToInt_2(s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += m[char]
        return number
    
print("Input: III")
print("Output: ", romanToInt_1("III"))
print("")
print("Input: LVIII")
print("Output: ", romanToInt_1("LVIII"))
print("")
print("Input: MCMXCIV")
print("Output: ", romanToInt_1("MCMXCIV"))
print("")

print("Input: III")
print("Output: ", romanToInt_2("III"))
print("")
print("Input: LVIII")
print("Output: ", romanToInt_2("LVIII"))
print("")
print("Input: MCMXCIV")
print("Output: ", romanToInt_2("MCMXCIV"))
print("")
