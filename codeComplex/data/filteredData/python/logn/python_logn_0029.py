def main(n: int):
    # 根据规模 n 生成测试数据：
    # 这里简单设定 a 和 b 为与 n 线性相关的两个整数，并保证 a != b。
    # 可根据需要修改生成方式。
    a = n
    b = 2 * n + 1  # 确保 b > a 且不同

    if a == b:
        # print(0)
        pass
        return

    e1 = bin(a)[2:]
    e2 = bin(b)[2:]
    diff = len(e2) - len(e1)
    e1 = ("0" * diff) + e1
    e1 = e1[::-1]
    e2 = e2[::-1]
    ans = ["0"] * len(e2)

    for i in range(len(e2)):
        if b - a >= 2 ** i:
            ans[i] = "1"

        else:
            if int(e1[i]) ^ int(e2[i]) == 1:
                ans[i] = "1"

    # print(int("".join(ans[::-1]), 2))
    pass
if __name__ == "__main__":
    # 示例：调用 main，规模 n 自行设定
    main(10)