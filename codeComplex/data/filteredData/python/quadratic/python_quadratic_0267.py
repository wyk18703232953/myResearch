import random

def main(n):
    # 生成测试数据：a 和 b 为长度为 n 的整数数组，元素范围 1~2n
    m = n  # 这里让 m 与 n 相同，也可按需调整
    a = [random.randint(1, 2 * n) for _ in range(n)]
    b = [random.randint(1, 2 * n) for _ in range(m)]

    lst = []
    for i in range(len(a)):
        if a[i] in b:
            lst.append(a[i])

    if len(lst) == 0:
        return
    else:
        print(*lst)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)