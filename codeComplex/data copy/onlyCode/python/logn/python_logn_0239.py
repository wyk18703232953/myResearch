def really_big(x):
    sum_digit = 0
    digits = x
    while digits > 0:
        sum_digit += digits % 10
        digits = digits // 10

    if x - sum_digit >= s:
        return True
    return False

def solve():
    left = 1
    right = n
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if really_big(mid): # mid is really big
            right = mid - 1
            ans = n - mid + 1
        else: # mid is not really big
            left = mid + 1
    return ans
"""
25 20
"""

n, s = map(int, input().split())
print(solve())
