# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.

# a -> e
# e -> a,i
# i -> a,e,o,u
# o -> i, u
# u -> a
 

# Example 1:

# Input: 
n1 = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
# Example 2:

# Input: 
n2 = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
# Example 3: 

# Input: 
n3 = 5
# Output: 68
 

### Time Limit Exceed ## 
def solve(char, n):
    if n == 0:
        return 1
    
    if char == "a":
        return solve("e", n - 1)
    elif char == "e":
        return solve("a", n - 1) + solve("i", n - 1)
    elif char == "i":
        return solve("a", n - 1) + solve("e", n - 1) + solve("o", n - 1) + solve("u", n - 1)
    elif char == "o":
        return solve("i", n - 1) + solve("u", n - 1)
    else:
        return solve("a", n - 1)

def countVowelPermutation(n: int) -> int:
    result = 0
    result += solve("a", n - 1)
    result += solve("e", n - 1)
    result += solve("i", n - 1)
    result += solve("o", n - 1)
    result += solve("u", n - 1)
    return result

# print(countVowelPermutation(n1))
# print(countVowelPermutation(n2))
# print(countVowelPermutation(n3))

### Time Limit Exceed ## 
def countVowelPermutation2(n: int) -> int:
        result = 0
        M = (10**9 + 7)
        a ,e, i, o, u = 0, 1, 2, 3, 4
        mem = [[-1]*n]*5
        def solve(char, n):
            print("[char][n]:[", char, "][", n,"] point", mem[char][n])
            if n == 0:
                return 1
            # if mem[char][n] != -1:
            #     # print("p", mem[char][n])
            #     return mem[char][n]
            if char == a:
                mem[char][n] = solve(e, n - 1)
            elif char == e:
                mem[char][n] = solve(a, n - 1) + solve(i, n - 1)
            elif char == i:
                mem[char][n] = solve(a, n - 1) + solve(e, n - 1) + solve(o, n - 1) + solve(u, n - 1)
            elif char == o:
                mem[char][n] = solve(i, n - 1) + solve(u, n - 1)
            else:
                mem[char][n] = solve(a, n - 1)
            # print("char:", char, "point", mem[char][n])
            return mem[char][n]
        # print(mem)


        result += solve(a, n - 1) 
        result += solve(e, n - 1)
        result += solve(i, n - 1)
        result += solve(o, n - 1)
        result += solve(u, n - 1)
        # print(mem)
        return result

# print(countVowelPermutation2(n1))
print(countVowelPermutation2(n2))
# print(countVowelPermutation2(n3))