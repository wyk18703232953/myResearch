import random

def main(n):
    # 生成测试数据：长度为 n 的正整数数组 b
    # 这里假设元素范围为 1~n，可根据需要调整
    b = [random.randint(1, n) for _ in range(n)]

    # 以下为原逻辑
    z = max(b)
    if z == 1:
        b[b.index(z)] = 2
    else:
        b[b.index(z)] = 1

    print(*sorted(b))


if __name__ == "__main__":
    # 示例：规模 n = 10，可按需修改或在外部调用 main(n)
    main(10)