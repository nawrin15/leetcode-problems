# Example 1:

# Input: 
seats1 = [3,1,5]
students1 = [2,7,4]
# Output: 4
# Explanation: The students are moved as follows:
# - The first student is moved from from position 2 to position 1 using 1 move.
# - The second student is moved from from position 7 to position 5 using 2 moves.
# - The third student is moved from from position 4 to position 3 using 1 move.
# In total, 1 + 2 + 1 = 4 moves were used.
# Example 2:

# Input: 
seats2 = [4,1,5,9]
students2 = [1,3,2,6]
# Output: 7
# Explanation: The students are moved as follows:
# - The first student is not moved.
# - The second student is moved from from position 3 to position 4 using 1 move.
# - The third student is moved from from position 2 to position 5 using 3 moves.
# - The fourth student is moved from from position 6 to position 9 using 3 moves.
# In total, 0 + 1 + 3 + 3 = 7 moves were used.
# Example 3:

# Input: 
seats3 = [2,2,6,6]
students3 = [1,3,2,6]
# Output: 4
# Explanation: Note that there are two seats at position 2 and two seats at position 6.
# The students are moved as follows:
# - The first student is moved from from position 1 to position 2 using 1 move.
# - The second student is moved from from position 3 to position 6 using 3 moves.
# - The third student is not moved.
# - The fourth student is not moved.
# In total, 1 + 3 + 0 + 0 = 4 moves were used.

def minMovesToSeat(seats, students) -> int:
    seats = sorted(seats)
    students = sorted(students)
    return sum([abs(seat-student) for seat, student in zip(seats, students)])

print(minMovesToSeat(seats1, students1))
print(minMovesToSeat(seats2, students2))
print(minMovesToSeat(seats3, students3))
