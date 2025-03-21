# Example 1:

# Input: 
time1 = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
# Example 2:

# Input: 
time2 = "0?:3?"
# Output: "09:39"
# Example 3:

# Input: 
time3 = "1?:22"
# Output: "19:22"
time4 ="?4:03"
#output: "14:03"
time5 = "?5:13"
#output: "15:13"

time6 = "??:3?"

def maximumTime(time: str) -> str:
    res = ""
    if time[0] == '?':
        if time[1] == "?":
            res += "2"
        elif int(time[1]) > 3:
            res += "1"
        else:
            res += "2"
    else:
        res += time[0]       
    if time[1] == '?':
        if res[0] == '2':
            res += '3'
        else:
            res += '9'
    else:
        res += time[1]
    res += ":"
    res += "5" if time[3] == '?' else time[3]
    res += "9" if time[4] == "?" else time[4]
    return res

print(maximumTime(time1))
print(maximumTime(time2))
print(maximumTime(time3))
print(maximumTime(time4))
print(maximumTime(time5))
print(maximumTime(time6))