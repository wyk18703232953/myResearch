from collections import Counter
import random

def main(n):
    # 生成测试数据：
    # n: 需要满足的数量
    # m: 不同元素的数量，设为 n 的一半向上取整（至少为 1）
    m = max(1, (n + 1) // 2)

    # 生成一个长度为 m 的数组，每个元素代表某个值出现的次数
    # 随机生成每个值出现的次数，保证总和至少为 n
    # 先随机生成基础次数
    base_counts = [random.randint(1, n) for _ in range(m)]
    total = sum(base_counts)
    if total < n:
        # 如果总和小于 n，则将差值加到第一个元素上
        base_counts[0] += n - total

    # 将 base_counts 展开成真正的“数组” a_list
    a_list = []
    for idx, cnt in enumerate(base_counts):
        a_list.extend([idx] * cnt)

    # 原程序逻辑开始
    # n: 需要的数量
    # m: 实际有 m 个数（这里与上面的 m 一致）
    m = len(a_list)

    # 统计每个数出现的次数
    a = Counter(a_list).values()

    i = 1
    while sum(x // i for x in a) >= n:
        i += 1
    ans = i - 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)