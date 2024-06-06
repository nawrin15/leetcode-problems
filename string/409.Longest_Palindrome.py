from collections import defaultdict, Counter


class Solution:
    def longestPalindrome1(self, s: str) -> int:
        counter = defaultdict(int)
        res = 0
        for i in s:
            counter[i] += 1
            if counter[i] % 2 == 0:
                res += 2 
        
        for count in counter.values():
            if count % 2 == 1:
                res += 1
                break
        return res


    def longestPalindrome2(self, s: str) -> int:
        seen = set()
        count = 0
        for c in s:
            if c in seen:
                seen.remove(c)
                count += 2
            else:
                seen.add(c)
                
        return count + 1 if seen else count   
    
    def longestPalindrome3(self, s: str) -> int:
        counter = Counter(s)
        odd_counter = 0
        for freq in counter:
            if counter[freq] % 2 == 1:
                odd_counter += 1

        return len(s) - odd_counter + 1 if odd_counter > 0 else len(s)  
        

a = Solution()

#Example 1:

#Input: 
s = "abccccdd"
print(a.longestPalindrome1(s))
print(a.longestPalindrome2(s))
print(a.longestPalindrome3(s))
#Output: 7
#Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

#Example 2:
#Input: 
s = "a"
print(a.longestPalindrome1(s))
print(a.longestPalindrome2(s))
print(a.longestPalindrome3(s))
#Output: 1
#Explanation: The longest palindrome that can be built is "a", whose length is 1.