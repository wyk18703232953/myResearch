import math

def validation(n, k, x):
    if (x * (x + 1)) // 2 - (n - x) == k:
        return 0
    if (x * (x + 1)) // 2 - (n - x) > k:
        return 1
    return 2

def run_once(n, k):
    l = 0
    r = 1000000001
    while True:
        mid = (l + r) // 2
        flag = validation(n, k, mid)
        if flag == 0:
            ans = mid
            break
        elif flag == 1:
            r = mid
        else:
            l = mid
    return n - ans

def main(n):
    results = []
    for i in range(1, n + 1):
        ni = i
        ki = (i * (i + 1)) // 4
        results.append(run_once(ni, ki))
    return results

if __name__ == "__main__":
    res = main(10)
    for v in res:
        print(v)