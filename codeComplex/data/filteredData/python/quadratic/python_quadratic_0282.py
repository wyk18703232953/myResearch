import random

def main(n: int):
    # 生成测试数据：l1 和 l2 为长度为 n 的整数列表，元素范围 1..2n
    m = n  # 保留原来 n,m 的结构，这里令 m = n
    l1 = [random.randint(1, 2 * n) for _ in range(n)]
    l2 = [random.randint(1, 2 * m) for _ in range(m)]

    # 与原始逻辑一致：顺序遍历 l1，若元素在 l2 中则输出
    for i in l1:
        if i in l2:
            print(i, end=" ")

if __name__ == "__main__":
    # 示例调用，可按需修改或在外部调用 main(n)
    main(5)