from functools import reduce
import random

def main(n: int):
    # 生成测试数据：
    # n 为元素个数，生成 n 对 (a, b)，以及一个容量 m
    # 约束：a, b 为非负整数；m 为正整数
    # 可根据需要修改数据分布
    pairs = []
    for _ in range(n):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        pairs.append((a, b))
    m = random.randint(0, max(1, sum(a for a, _ in pairs)))  # 容量适当范围内

    # 下面是原逻辑的无 input() 改写
    entries = []
    for a, b in pairs:
        entries.append((a, b, a - b))

    entries.sort(key=lambda x: x[2], reverse=True)

    size = reduce(lambda s, e: s + e[0], entries, 0)
    count = 0

    while size > m and count < n:
        size -= entries[count][2]
        count += 1

    result = -1 if size > m else count
    print(result)
    return result

if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)