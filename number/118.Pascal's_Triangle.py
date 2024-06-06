class Solution:
    def generate(self, numRows: int):
        triangle = [[1]]
        for i in range(numRows - 1):
            temp = [0] + triangle[-1] + [0]
            each_row = []
            for j in range(len(triangle[-1]) + 1 ):
                each_row.append(temp[j+1] + temp[j])
            triangle.append(each_row)
        return triangle

a = Solution()
#Example 1:
#Input: 
numRows = 5
print(a.generate(numRows))
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#Example 2:

#Input: 
numRows = 1
print(a.generate(numRows))
#Output: [[1]]