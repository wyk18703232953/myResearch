from collections import Counter
import random

def main(n: int):
    # 生成测试数据：
    # 随机选择 c，数组 a 中的元素范围为 [1, max(2, n//2)]
    if n <= 0:
        return

    val_range = max(2, n // 2)
    c = random.randint(1, val_range)
    a = [random.randint(1, val_range) for _ in range(n)]

    # 原始逻辑开始
    counter = Counter()
    minus = 0
    count = a.count(c)
    maxi = 0

    for i in range(n):
        if a[i] != c:
            if counter[a[i]] < minus:
                counter[a[i]] = minus
            counter[a[i]] += 1
            maxi = max(maxi, counter[a[i]] + count - minus)
        else:
            minus += 1

    print(max(maxi, minus))


if __name__ == "__main__":
    # 示例：规模为 10，可根据需要修改
    main(10)