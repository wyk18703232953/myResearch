import random

def main(n: int):
    # 生成测试数据
    # n: 需要满足的总数量
    # 我们生成一个长度为 m 的数组 a，元素值在 1..n 之间
    # 可根据需要调整 m 与 n 的关系
    m = 2 * n  # 示例：令 m 为 2n
    a = [random.randint(1, n) for _ in range(m)]

    # 原始逻辑
    cnt = {}
    for x in a:
        cnt[x] = cnt.get(x, 0) + 1

    k = 1
    while sum(v // k for v in cnt.values()) >= n:
        k += 1

    print(k - 1)


if __name__ == "__main__":
    # 示范调用：规模为 10
    main(10)