import random

def main(n: int):
    # 生成测试数据：
    # n: 给定规模
    # pos: [1, n]
    # l, r: 1 <= l <= r <= n
    pos = random.randint(1, n)
    l = random.randint(1, n)
    r = random.randint(l, n)

    result = abs(pos - l) + r - l + 2
    if l == 1:
        if abs(pos - r) + 1 < result:
            result = abs(pos - r) + 1
    if r == n:
        if abs(pos - l) + 1 < result:
            result = abs(pos - l) + 1
    if l == 1 and r == n:
        result = 0
    if abs(pos - r) + r - l + 2 < result:
        result = abs(pos - r) + r - l + 2

    print(result)


if __name__ == "__main__":
    # 示例：调用 main，n 可按需修改
    main(10)