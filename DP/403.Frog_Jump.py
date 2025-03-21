
# Input: 
stones1 = [0,1,3,5,6,8,12,17]
# Output: true
# Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
# Example 2:

# Input: 
stones2 = [0,1,2,3,4,8,9,11]
# Output: false
# Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.


def canCross(stones) -> bool:
    prev = 1
    for i in range(len(stones)-1):
        diff = stones[i+1] - stones[i] 
        if not ((diff == prev - 1) or (diff == prev) or (diff == prev + 1)):
            print(diff)
            print(prev)
            return False
        prev = diff
    return True


print(canCross(stones1))
    