# Example 1:

# Input: 
paths1 = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# Output: "Sao Paulo" 
# Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
# Example 2:

# Input: 
paths2 = [["B","C"],["D","B"],["C","A"]]
# Output: "A"
# Explanation: All possible trips are: 
# "D" -> "B" -> "C" -> "A". 
# "B" -> "C" -> "A". 
# "C" -> "A". 
# "A". 
# Clearly the destination city is "A".
# Example 3:

# Input: 
paths3 = [["A","Z"]]
# Output: "Z"

def destCity(paths) -> str:
    source = set()
    destination = set()
    for path in paths:
        source.add(path[0])
        destination.add(path[1])
    return (destination - source).pop()

print(destCity(paths1))
print(destCity(paths2))
print(destCity(paths3))