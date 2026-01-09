def fun(n, ptr1, a):
    if n == 1:
        a[ptr1] = 1
    elif n == 2:
        a[ptr1] = 1
        ptr1 += 1
        a[ptr1] = 2
    elif n == 3:
        a[ptr1] = 1
        ptr1 += 1
        a[ptr1] = 1
        ptr1 += 1
        a[ptr1] = 3

    else:
        itera = n - n // 2

        for _ in range(itera):
            a[ptr1] = 1
            ptr1 += 1

        fun(n // 2, ptr1, a)
        for _ in range(n // 2):
            a[ptr1] = 2 * a[ptr1]
            ptr1 += 1


def main(n):
    # 根据 n 生成测试数据，这里直接使用 n 作为规模
    a = [0] * n
    fun(n, 0, a)
    for v in a:
        # print(v, end=" ")
        pass
    # print()
    pass
if __name__ == "__main__":
    # 示例：可自行修改 n 进行测试
    main(10)