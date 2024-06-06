class Solution:
    def condition(self, num):
        if num % 5 == 0 and num % 3 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        return str(num)
    
    def fizzBuzz1(self, n: int):
        return [self.condition(i + 1) for i in range(n)]
    
    def fizzBuzz2(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
    
    def fizzBuzz3(self, n: int):
        f, b, fb = 'Fizz', 'Buzz', 'FizzBuzz'
        arr = [str(x + 1) for x in range(n)]
        
        for i in range(2, n, 3):
            arr[i] = f
        
        for i in range(4, n, 5):
            arr[i] = b
        
        for i in range(14, n, 15):
            arr[i] = fb
        
        return arr

a = Solution()
#Example 1:

#Input: 
n = 3
print(a.fizzBuzz1(n))
print(a.fizzBuzz2(n))
#Output: ["1","2","Fizz"]

#Example 2:
#Input: 
n = 5
print(a.fizzBuzz1(n))
print(a.fizzBuzz2(n))
#Output: ["1","2","Fizz","4","Buzz"]

#Example 3:
#Input: 
n = 15
print(a.fizzBuzz1(n))
print(a.fizzBuzz2(n))
#Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]