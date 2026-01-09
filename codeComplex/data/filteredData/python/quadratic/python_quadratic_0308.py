import math
import collections

def main(n):
    # Interpret n as the length of the array; also set k deterministically
    if n <= 0:
        return
    k = max(1, n // 3)
    arr = [(i * 7 + 3) % 100 for i in range(n)]

    ans = 0
    for i in range(n):
        val = arr[i]
        c = 1
        sol = 0
        if c >= k:
            sol = max(sol, val / c)
        for j in range(i + 1, n):
            val += arr[j]
            c += 1
            if c >= k:
                sol = max(sol, val / c)
        ans = max(sol, ans)
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)