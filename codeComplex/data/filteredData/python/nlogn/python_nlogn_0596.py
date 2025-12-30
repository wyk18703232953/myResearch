import random

def main(n):
    # 生成测试数据
    # 规模 n：数组长度
    # 为保证算法逻辑，与原始代码类似地再生成 m（未实际使用，但保持形式一致）
    m = n  # 若原题中 m 有其它含义，可在此调整
    a = [random.randint(0, 10) for _ in range(n)]

    # 原始逻辑开始
    ans = sum(a)
    a.sort()
    lastlevel = 0
    level = 0
    got = 0

    for i in a:
        got = max(got, i)
        level = min(level + 1, got)
        if i > 0:
            ans -= 1
            lastlevel = level

    ans -= (got - level)
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)