def main(n: int):
    import random

    # 根据 n 生成测试数据
    # 这里设定 m = n（你也可以按需要调整为其他函数关系）
    m = n

    # 随机生成 n 个长度为 m 的 0/1 字符串
    A = []
    for _ in range(n):
        row = ''.join(random.choice('01') for _ in range(m))
        A.append(row)

    # 以下为原程序逻辑，仅去掉了 input()，并放入 main 中
    C = [0] * m
    for i in range(n):
        a = A[i]
        for j, c in enumerate(a):
            C[j] += int(c)

    for i in range(n):
        a = A[i]
        for j, c in enumerate(a):
            C[j] -= int(c)
        for j in range(m):
            if C[j] == 0:
                break
        else:
            print('YES')
            return
        for j, c in enumerate(a):
            C[j] += int(c)
    print('NO')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)