from collections import Counter

class Solution:
	def findTheDifference1(self, s: str, t: str) -> str:
		print("Using Counter")
		print("=============")
		print("s-", Counter(s))
		print("t-", Counter(t))
		print("Diff", Counter(t)-Counter(s))
		print("Diff list", list(Counter(t)-Counter(s)))
		print("Result::::")
		return list(Counter(t) - Counter(s))[0]
	
	def findTheDifference2(self, s:str, t:str) -> str:
		print("Using Sort")
		s, t = sorted(s), sorted(t)
		print("sorted s::", s)
		print("sorted t::", t)
		for i, j in enumerate(s):
			print("i, j, t[i] = ", i, j, t[i])
			if j != t[i]:
				return t[i]
		return t[-1]
	
	def findTheDifference3(self, s:str, t:str) -> str:
		print(set(t))
		for i in set(t):
			print("s.count(i) - ", s.count(i))
			print("t.count(i) - ", t.count(i))
			print("i - ", i)
			if s.count(i) != t.count(i):
				return i 
			

a = Solution()
#Example 1:

#Input: 
s = "abcd"
t = "abcde"
print(a.findTheDifference1(s, t))
print(a.findTheDifference2(s, t))
print(a.findTheDifference3(s, t))
#Output: "e"
#Explanation: 'e' is the letter that was added.


#Example 2:

#Input: 
s = ""
t = "y"
print(a.findTheDifference1(s, t))
print(a.findTheDifference2(s, t))
print(a.findTheDifference3(s, t))
#Output: "y"
		
			
    