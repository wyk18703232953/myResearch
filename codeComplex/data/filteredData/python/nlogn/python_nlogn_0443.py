from collections import defaultdict as dd
import random

def main(n):
    # 生成测试数据
    # 随机生成 m，保证在 1..n 范围内，方便构造包含 m 的数组
    if n <= 0:
        return

    m = random.randint(1, n)

    # 构造数组：保证至少有一个元素等于 m
    arr = []
    for _ in range(n - 1):
        # 随机生成相对 m 的位置：小于、等于、大于
        t = random.randint(0, 2)
        if t == 0:      # 小于 m
            val = m - random.randint(1, 5)
        elif t == 1:    # 等于 m
            val = m
        else:           # 大于 m
            val = m + random.randint(1, 5)
        arr.append(val)
    # 保证至少有一个 m
    arr.append(m)
    random.shuffle(arr)

    # 原始逻辑
    d = dd(int)
    has = False
    count = 0
    d[0] = 1
    total = 0

    for i in range(n):
        if arr[i] > m:
            count += 1
        if arr[i] < m:
            count -= 1
        if arr[i] == m:
            has = True
        if has:
            total += d[count] + d[count - 1]
        else:
            d[count] += 1

    print(total)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)