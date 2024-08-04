# Example 1:

# Input: 
details1 = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# Output: 2
# Explanation: The passengers at indices 0, 1, and 2 have ages 75, 92, and 40. Thus, there are 2 people who are over 60 years old.
# Example 2:

# Input: 
details2 = ["1313579440F2036","2921522980M5644"]
# Output: 0
# Explanation: None of the passengers are older than 60.

def countSeniors(details) -> int:
    count = 0
    for detail in details:
        if int(detail[-4:-2]) > 60:
            count += 1
    return count

print(countSeniors(details1))
print(countSeniors(details2))


def countSeniors2(details) -> int:
    return sum([1 if int(detail[-4:-2]) > 60 else 0 for detail in details])


print(countSeniors2(details1))
print(countSeniors2(details2))