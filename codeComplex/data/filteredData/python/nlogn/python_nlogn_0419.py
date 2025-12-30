from collections import defaultdict
import random


def main(n: int):
    """
    生成 n 个随机区间并执行原逻辑。
    可根据需要修改生成规则。
    """
    # -------- 1. 生成测试数据（n 个区间）--------
    # 示例策略：在 [1, 3n] 内生成 n 个随机区间，保证 l <= r
    intervals = []
    for _ in range(n):
        l = random.randint(1, 3 * n)
        r = random.randint(1, 3 * n)
        if l > r:
            l, r = r, l
        intervals.append((l, r))

    # -------- 2. 原逻辑改写（去掉 input）--------
    s = []
    for a0, a1 in intervals:
        s += [(a0, 0), (a1, 1)]
    s.sort()
    now = 0
    rev = defaultdict(int)

    for a, b in zip(s, s[1:]):
        if a[1] == 0:
            now += 1
            rev[now] += b[0] - a[0]
            if b[1] == 1:
                rev[now] += 1
        else:
            now -= 1
            if b[0] != a[0]:
                rev[now] += b[0] - a[0]
                if b[1] == 0:
                    rev[now] -= 1

    # -------- 3. 输出结果 --------
    for i in range(1, n + 1):
        print(rev[i], end=" ")
    print()  # 换行，便于多次调用观察


if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)