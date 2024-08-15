# Example 1:

# Input: 
mountain1 = [2,4,4]
# Output: []
# Explanation: mountain[0] and mountain[2] can not be a peak because they are first and last elements of the array.
# mountain[1] also can not be a peak because it is not strictly greater than mountain[2].
# So the answer is [].
# Example 2:

# Input: 
mountain2 = [1,4,3,8,5]
# Output: [1,3]
# Explanation: mountain[0] and mountain[4] can not be a peak because they are first and last elements of the array.
# mountain[2] also can not be a peak because it is not strictly greater than mountain[3] and mountain[1].
# But mountain [1] and mountain[3] are strictly greater than their neighboring elements.
# So the answer is [1,3].

def findPeaks(mountain):
    res = []
    for i in range(1, len(mountain) - 1):
        if mountain[i] > mountain[i + 1]:
            res.append(i)
    return res

print(findPeaks(mountain1))
print(findPeaks(mountain2))