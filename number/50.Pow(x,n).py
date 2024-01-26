def pow(x, n):
    def helper(x, n):
        if x == 0: return 0
        if n == 0: return 1
        
        result = helper(x * x, n//2)
        
        return result if n % 2 == 0 else result * x  ## if odd power ex. 5 ==> 5//2 ==> 2 + 1
    
    result = helper(x, abs(n))
    return 1 / result if n < 0 else result # if power is negative pow(x, -n) ==> x^-n ==> 1/x^n

print(pow(10, 100))