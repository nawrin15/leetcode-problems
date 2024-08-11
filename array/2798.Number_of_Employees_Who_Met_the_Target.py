# Example 1:

# Input: 
hours1 = [0,1,2,3,4]
target1 = 2
# Output: 3
# Explanation: The company wants each employee to work for at least 2 hours.
# - Employee 0 worked for 0 hours and didn't meet the target.
# - Employee 1 worked for 1 hours and didn't meet the target.
# - Employee 2 worked for 2 hours and met the target.
# - Employee 3 worked for 3 hours and met the target.
# - Employee 4 worked for 4 hours and met the target.
# There are 3 employees who met the target.
# Example 2:

# Input: 
hours2 = [5,1,4,2,2]
target2 = 6
# Output: 0
# Explanation: The company wants each employee to work for at least 6 hours.
# There are 0 employees who met the target.

def numberOfEmployeesWhoMetTarget(hours, target: int) -> int:
    # count = 0
    # for h in hours:
    #     if h >= target:
    #         count += 1
    # return count
    # return sum([1 if h >= target else 0 for h in hours])
    # return sum([1 for h in hours if h >= target])
    return len([1 for h in hours if h >= target])

print(numberOfEmployeesWhoMetTarget(hours1, target1))
print(numberOfEmployeesWhoMetTarget(hours2, target2))