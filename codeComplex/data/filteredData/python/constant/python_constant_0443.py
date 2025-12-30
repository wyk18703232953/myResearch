import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里假设原本的 m 在后续逻辑中并未使用，仅作为输入存在
    # 为保证通用性，生成一个与 n 同规模量级的 m
    m = random.randint(1, max(1, n * 2))

    # 原始逻辑：只使用了 n
    print(n * "8")
    if n >= 1:
        print((n - 1) * "1" + "2")
    else:
        # 当 n <= 0 时，原代码行为未定义，这里不输出第二行
        pass

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)