class Solution:
    def getRow(self, rowIndex: int):
        row = [1]
        for i in range(rowIndex):
            next_row = [0] * (len(row) + 1)
            for j in range(len(row)):
                next_row[j] += row[j]
                next_row[j + 1] += row[j]
            row = next_row
        return row

a = Solution()

#Example 1:

#Input: 
rowIndex = 3
print(a.getRow(rowIndex))

#Output: [1,3,3,1]
#Example 2:

#Input: 
rowIndex = 0
print(a.getRow(rowIndex))

#Output: [1]
#Example 3:

#Input: 
rowIndex = 1
print(a.getRow(rowIndex))

#Output: [1,1]