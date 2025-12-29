import sys
import random

def solve(l, c):
    n = len(l)
    a = []
    for i in range(1, n - 1):
        lr = sys.maxsize
        lc = sys.maxsize
        for j in range(0, i):
            if l[i] > l[j]:
                lc = min(lc, c[j])
        for j in range(i + 1, n):
            if l[j] > l[i]:
                lr = min(lr, c[j])
        if lr < sys.maxsize and lc < sys.maxsize:
            a.append(lr + lc + c[i])
    if not a:
        return -1
    else:
        return min(a)

def main(n):
    # 生成测试数据：
    # l 为 1 到 10^6 之间的不重复随机整数
    # c 为 1 到 100 之间的随机整数
    if n < 3:
        # 原逻辑在 n<3 时无法形成中间元素，直接返回 -1
        print(-1)
        return

    # 为保证有一定的递增关系，先生成一个递增序列再随机打乱或调整
    l = sorted(random.sample(range(1, 10**6), n))
    # 也可以选择不打乱，使得更容易产生满足条件的三元组
    # random.shuffle(l)  # 如需更随机的测试数据，可取消注释

    c = [random.randint(1, 100) for _ in range(n)]

    ans = solve(l, c)
    print(ans)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)