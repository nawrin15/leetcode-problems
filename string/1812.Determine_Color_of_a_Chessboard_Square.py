# Example 1:

# Input: 
coordinates1 = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
# Example 2:

# Input: 
coordinates2 = "h3"
# Output: true
# Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
# Example 3:

# Input: 
coordinates3 = "c7"
# Output: false

def squareIsWhite(coordinates: str) -> bool:
    l1 = ord(coordinates[0]) - 96
    l2 = int(coordinates[1])
    return (l1 + l2) % 2


print(squareIsWhite(coordinates1))
print(squareIsWhite(coordinates2))
print(squareIsWhite(coordinates3))