from collections import defaultdict
import random

def f(d, n):
    res = 0
    prev = None
    ans = [0] * (n + 1)
    for i in sorted(d.keys()):
        if prev is None:
            prev = i
        else:
            ans[res] += i - prev
            prev = i
        res += d[i]
    return ans[1:]

def main(n):
    # 生成测试数据：n 个区间 [x, y]，其中 1 <= x <= y <= n
    d = defaultdict(int)
    for _ in range(n):
        x = random.randint(1, n)
        y = random.randint(x, n)
        d[x] += 1
        d[y + 1] -= 1

    result = f(d, n)
    print(*result)

if __name__ == "__main__":
    # 示例：可修改 n 以改变规模
    main(10)