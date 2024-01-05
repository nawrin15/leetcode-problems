####334. Increasing Triplet Subsequence

nums = [1,2,3,4,5]
nums = [2,1,5,0,4,6]
# nums = [5,4,3,2,1]
first = second = float('inf')

for i in nums:
    if i <= first:
        first = i
    elif i <= second:
        second = i
    else:
        print(True)
    
print(False)