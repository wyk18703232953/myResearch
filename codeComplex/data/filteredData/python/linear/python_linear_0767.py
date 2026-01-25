INF = 1000_000_000
from collections import deque

def main(n):
    # 映射规则：
    # n >= 2 时：
    #   数组长度 = n
    #   查询数量 q = n
    #   查询 m 从 1 到 q 依次递增
    # n < 2 时：退化成最小可运行规模 n = 2
    if n < 2:
        n = 2
    q = n
    arr = [i + 1 for i in range(n)]
    maxval = max(arr)
    d = deque(arr)
    ans = {}
    count = 1
    while d[0] != maxval:
        a = d.popleft()
        b = d.popleft()
        ans[count] = (a, b)
        count += 1
        d.append(min(a, b))
        d.appendleft(max(a, b))
    n = n - 1
    outputs = []
    for i in range(q):
        m = i + 1
        if m in ans:
            outputs.append(f"{ans[m][0]} {ans[m][1]}")
        else:
            mm = m - count
            outputs.append(f"{maxval} {d[1 + (mm % n)]}")
    print("\n".join(outputs))

if __name__ == "__main__":
    main(10)