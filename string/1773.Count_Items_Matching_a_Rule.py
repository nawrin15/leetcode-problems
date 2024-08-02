# Example 1:

# Input: 
items1 = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey1 = "color"
ruleValue1 = "silver"
# Output: 1
# Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
# Example 2:

# Input: 
items2 = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey2 = "type"
ruleValue2 = "phone"
# Output: 2
# Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.

def countMatches(items, ruleKey, ruleValue) -> int:
        rules = {
            "type": 0,
            "color": 1,
            "name" : 2
        }
        index = rules[ruleKey]
        return sum(item[index] == ruleValue for item in items)


print(countMatches(items1, ruleKey1, ruleValue1))
print(countMatches(items2, ruleKey2, ruleValue2))