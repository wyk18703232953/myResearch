def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def main(n):
    # 根据规模 n 生成测试数据，这里直接使用 n 作为测试输入
    x = n

    ans = 0
    if x == 1:
        ans = 1
    elif x == 2:
        ans = 2
    else:
        if x % 2 != 0:
            ans = x * (x - 1) * (x - 2)
        else:
            if gcd(x, x - 3) == 1:
                ans = x * (x - 1) * (x - 3)
            else:
                ans = (x - 1) * (x - 2) * (x - 3)

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)