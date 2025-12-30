import random

def main(n: int):
    # 随机生成测试数据：a、b 两个长度为 n 的整数数组
    # 元素范围可自行调整，这里设为 1~2n
    m = n  # 若需要不同规模，可自行修改为与 n 不同的值
    a = [random.randint(1, 2 * n) for _ in range(n)]
    b = [random.randint(1, 2 * n) for _ in range(m)]

    r = []
    for i in a:
        if i in b:
            r.append(i)

    # 按原逻辑输出结果
    print(' '.join(map(str, r)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)