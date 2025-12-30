import random

def main(n: int):
    # 生成测试数据：
    # x 和 y 为长度为 n 的整数列表，元素范围为 1..2n
    # 可根据需要修改生成逻辑
    m = n  # 原代码中 m 未被实际使用，这里令 m = n 以保持结构
    x = [random.randint(1, 2 * n) for _ in range(n)]
    y = [random.randint(1, 2 * n) for _ in range(m)]

    xx = set(x)
    yy = set(y)
    common = xx.intersection(yy)
    for i in x:
        if i in common:
            print(i, end=' ')


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)