import random

def main(n):
    # 生成测试数据：
    # a 和 b 都为长度为 n 的数组，元素范围 [1, 2n]
    m = n
    a = [random.randint(1, 2 * n) for _ in range(n)]
    b = [random.randint(1, 2 * n) for _ in range(m)]

    # 原逻辑：输出 a 中在 b 里的元素，按 a 的顺序
    result = []
    for x in a:
        if x in b:
            result.append(str(x))
    print(' '.join(result))


if __name__ == "__main__":
    # 示例：可按需修改规模
    main(5)