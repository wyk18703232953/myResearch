from collections import Counter
import random


def main(n):
    # 生成测试数据：
    # 随机选择一个值作为 c，接着生成长度为 n 的数组 a，其中元素范围在 1..n 之间
    if n <= 0:
        print(0)
        return

    c = random.randint(1, max(1, n // 2))  # 假设 c 较常出现
    a = [random.randint(1, n) for _ in range(n)]

    tel = Counter()
    target_count_last = Counter()
    targets = 0
    best = 0

    for num in a:
        if num == c:
            targets += 1
        else:
            since_last = targets - target_count_last[num]
            target_count_last[num] = targets
            tel[num] = max(0, tel[num] - since_last)
            tel[num] += 1
            best = max(best, tel[num])

    print(targets + best)


if __name__ == "__main__":
    # 示例：可在此处修改 n 进行本地测试
    main(10)