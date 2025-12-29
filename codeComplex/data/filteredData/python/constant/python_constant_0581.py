import random

def main(n: int):
    # 根据规模 n 生成测试数据 (x, y)
    # 保证 1 <= x, y <= n
    x = random.randint(1, n)
    y = random.randint(1, n)

    ans = (x - 1) + (y - 1) <= (n - x) + (n - y)
    print('White' if ans else 'Black')


if __name__ == "__main__":
    # 示例：可修改这里的 n 来进行测试
    main(8)