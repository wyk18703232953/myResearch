import collections
import sys

def can_win(i, dp):
    if i in dp:
        return dp[i]
    else:
        for next in possible[i]:
            if not can_win(next, dp):
                dp[i] = True
                return True
        dp[i] = False
        return False

data = sys.stdin.readlines()
nb = int(data[0])
nums = data[1].split(' ') 
nums = [int(c) for c in nums]
possible = [[] for _ in range(nb)]
for i in range(nb):
    if nums[i] == 1:
        possible[i] = [k for k in range(nb) if k != i] 
    else:
        for j in range(i+nums[i], nb, nums[i]):
            if nums[j] > nums[i]:
                possible[i].append(j)
        for j in range(i-nums[i], -1, -nums[i]):
            if nums[j] > nums[i]:
                possible[i].append(j)

res = ""
dp = {}
for i in range(nb):
    if can_win(i, dp):
        res += "A"
    else:
        res += "B"
print(res)
        
