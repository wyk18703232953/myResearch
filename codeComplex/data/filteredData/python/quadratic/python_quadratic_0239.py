import random

def solve(s, c):
    maxx = float('inf')
    n = len(s)
    ans = maxx
    for mid in range(1, n - 1):
        l = [maxx] + [c[i] for i in range(mid) if s[i] < s[mid]]
        r = [maxx] + [c[i] for i in range(mid + 1, n) if s[i] > s[mid]]
        ans = min(ans, min(l) + c[mid] + min(r))
    return ans if ans != float('inf') else -1


def main(n):
    # 生成测试数据：
    # s 为严格递增的整数序列，长度为 n
    # c 为对应的正权值
    if n < 3:
        # 原逻辑在 n<3 时循环不执行，相当于返回 -1
        s = list(range(n))
        c = [1] * n
        print(-1)
        return

    # 随机生成严格递增的 s
    base = random.randint(0, 10)
    step = random.randint(1, 5)
    s = [base + i * step + random.randint(0, 2) for i in range(n)]
    s.sort()

    # 随机生成费用数组 c
    c = [random.randint(1, 10) for _ in range(n)]

    ans = solve(s, c)
    print(ans)


if __name__ == "__main__":
    # 示例：可修改 n 做简单测试
    main(5)