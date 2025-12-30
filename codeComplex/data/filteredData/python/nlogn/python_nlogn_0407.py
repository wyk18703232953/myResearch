import random
from collections import defaultdict as dd

def main(n):
    # 生成 n 组区间 [l, r]，保证 l <= r
    # 这里生成的坐标范围可以按需调整
    intervals = []
    MAX_COORD = max(2 * n, 1)  # 防止 n=0 异常，且使规模随 n 变化

    for _ in range(n):
        l = random.randint(1, MAX_COORD)
        r = random.randint(1, MAX_COORD)
        if l > r:
            l, r = r, l
        intervals.append((l, r))

    d = dd(int)
    for l, r in intervals:
        d[l] += 1
        d[r + 1] -= 1

    arr = list(d.keys())
    arr.sort()
    ans = [0 for _ in range(n + 1)]
    count = 0
    l_arr = len(arr)
    arr.append(arr[-1])
    for i in range(l_arr):
        count += d[arr[i]]
        if 0 <= count <= n:  # 理论上 count 不会越界，但做个防护
            ans[count] += arr[i + 1] - arr[i]

    # 原程序输出 ans[1:]
    print(*ans[1:])

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)