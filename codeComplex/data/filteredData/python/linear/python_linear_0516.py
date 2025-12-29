import random

def main(n: int) -> int:
    # 生成测试数据：长度为 n 的 0/1 序列
    a = [random.randint(0, 1) for _ in range(n)]
    b = [random.randint(0, 1) for _ in range(n)]

    res = 0

    for j in range(n - 1):
        if (a[j] == 0) and (a[j + 1] == 1) and (b[j] == 1) and (b[j + 1] == 0):
            res += 1
            a[j] = 1
            a[j + 1] = 0
        elif (a[j] == 1) and (a[j + 1] == 0) and (b[j] == 0) and (b[j + 1] == 1):
            res += 1
            a[j] = 0
            a[j + 1] = 1

    for j in range(n):
        if a[j] != b[j]:
            res += 1

    print(res)
    return res

if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)