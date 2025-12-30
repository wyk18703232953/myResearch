import random

def main(n: int) -> None:
    # 生成测试数据：长度为 n 的数组 a，元素在 [1, n] 范围内
    m = n
    a = [random.randint(1, n) for _ in range(m)]

    b = [0] * n
    for i in a:
        b[i - 1] += 1
    b.sort()
    print(b[0])


if __name__ == "__main__":
    # 示例调用，可按需修改 n 的大小进行测试
    main(10)