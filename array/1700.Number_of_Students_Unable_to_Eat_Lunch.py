# Example 1:

# Input: 
students1 = [1,1,0,0]
sandwiches1 = [0,1,0,1]
# Output: 0 
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.
# Example 2:

# Input: 
students2 = [1,1,1,0,0,1]
sandwiches2 = [1,0,0,0,1,1]
# Output: 3

from collections import Counter

def countStudents(students, sandwiches) -> int:
    res = len(students)
    count = Counter(students)
    for s in sandwiches:
        if count[s] > 0:
            count[s] -= 1
            res -= 1 
        else:
            return res
    return res

print(countStudents(students1, sandwiches1))
print(countStudents(students2, sandwiches2))