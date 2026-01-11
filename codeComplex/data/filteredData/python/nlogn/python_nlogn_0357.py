from math import gcd

mod = 10**9 + 7

def lcd(xnum1, xnum2):
    return (xnum1 * xnum2 // gcd(xnum1, xnum2))

dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1]

def solve(arr):
    for i in arr:
        for k in range(31):
            if i - (1 << k) in arr and i + (1 << k) in arr:
                return [i - (1 << k), i, i + (1 << k)]
    for i in arr:
        for k in range(31):
            if i + (1 << k) in arr:
                return [i, i + (1 << k)]
    for i in arr:
        return [i]
    return []

def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    # 确定性生成 n 个整数，模拟原程序的 n 和后续输入
    arr = set(i for i in range(1, n + 1))
    lst = solve(arr)
    # print(len(lst))
    pass
    for x in lst:
        # print(x, end=' ')
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)