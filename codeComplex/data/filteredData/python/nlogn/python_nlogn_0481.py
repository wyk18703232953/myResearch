from collections import Counter
import random

def main(n: int):
    # 根据 n 生成测试数据：
    # 生成 m（数组长度），这里设为 2*n，至少保证有一定重复元素
    m = 2 * n

    # 生成数组 A，元素值范围 1..n（可根据需要调整）
    A = [random.randint(1, n) for _ in range(m)]

    # 原始逻辑开始
    C = Counter(A)

    def is_ok(x):
        cnt = 0
        for v in C.values():
            cnt += v // x
        return cnt >= n

    ok = 0
    ng = 1000
    while ok + 1 < ng:
        c = (ok + ng) // 2
        if is_ok(c):
            ok = c
        else:
            ng = c

    print(ok)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)