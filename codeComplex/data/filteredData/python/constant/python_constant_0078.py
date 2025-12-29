import random

def main(n: int):
    # 根据 n 生成测试数据，这里示例：生成一个与 n 相关的随机数 m
    # 你也可以根据需求将 m 设为 n 本身或其他函数，例如 m = n
    m = random.randint(1, max(3, n))

    # 将原逻辑作用在 m 上
    if m < 3:
        result = m
    else:
        if m % 2 != 0:
            result = m * (m - 1) * (m - 2)
        elif m % 3 == 0:
            result = (m - 1) * (m - 2) * (m - 3)
        else:
            result = m * (m - 1) * (m - 3)

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改
    main(10)