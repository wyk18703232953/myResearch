import random

def main(n: int):
    # 生成测试数据：长度为 n 的数组，元素为 1~10 的随机整数
    a = [random.randint(1, 10) for _ in range(n)]

    a.sort()
    if a[n - 1] == 1:
        a[n - 1] += 1
    else:
        a[n - 1] = 1
    a.sort()
    print(*a)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)