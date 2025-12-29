import random

def main(n: int):
    # 根据 n 生成测试数据，这里原逻辑是读取一个整数并加 1
    # 我们用 n 作为原输入，保持规模含义清晰
    x = n + 1

    if x == 1:
        print(0)
    else:
        if x % 2:
            print(x)
        else:
            print(x // 2)


if __name__ == "__main__":
    # 示例：根据规模 n 随机生成一个测试规模，并调用 main
    # 这里简单地使用一个固定或随机的 n，实际使用中可按需修改
    test_n = random.randint(0, 100)  # 生成一个 0~100 的规模作为示例
    main(test_n)