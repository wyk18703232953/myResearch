import random

def main(n: int):
    # 生成测试数据：n 行，每行 4 个 1~100 的随机整数
    r = []
    for _ in range(n):
        a, b, c, d = [random.randint(1, 100) for _ in range(4)]
        r.append(a + b + c + d)

    thomas = r[0]
    rank = sorted(r, reverse=True).index(thomas) + 1
    print(rank)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)