import random

def main(n):
    # 根据规模 n 生成测试数据，这里简单设定 k 为 1 到 n 之间的随机整数
    if n <= 0:
        return
    k = random.randint(1, n)

    if k == 1:
        print("1" + "0" * (n - 1))
    elif 3 * k <= n:
        print(
            ("0" * ((n - k) // 2))
            + "1"
            + ("0" * (k - 2))
            + "1"
            + "0" * ((n - k) // 2)
        )
    else:
        tmp = "0" * ((n - k) // 2) + "1"
        s = tmp
        s = tmp * (n // len(tmp) + 1)
        s = s[:n]
        print(s)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)