import random

def main(n: int):
    # 生成测试数据：长度为 n 的正整数数组
    # 数值范围可根据需要调整，这里设为 1~10
    a = [random.randint(1, 10) for _ in range(n)]

    a.sort()
    if a[-1] == 1:
        ans = a[:-1] + [2]
    else:
        ans = [1] + a[:-1]

    print(*ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)