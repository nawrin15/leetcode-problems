# Example 1:
# Input: 
s1 = "EEEEEEE"
# Output: 7
# Explanation:
# After each second, a person enters the waiting room and no person leaves it. 
# Therefore, a minimum of 7 chairs is needed.
# Example 2:

# Input: 
s2 = "ELELEEL"
# Output: 2
# Explanation:
# Let's consider that there are 2 chairs in the waiting room. The table below shows the state 
# of the waiting room at each second.
# Example 3:

# Input: 
s3 = "ELEELEELLL"

# Output: 3

# Explanation:

# Let's consider that there are 3 chairs in the waiting room. The table below shows the state of the waiting room at each second.

def minimumChairs(s: str) -> int:
    maxi = count = 0
    for i in s:
        if i == "E":
            count += 1
        elif i == "L":
            count -= 1
        if count > maxi:
            maxi = count
    return maxi


print(minimumChairs(s1))
print(minimumChairs(s2))
print(minimumChairs(s3))
