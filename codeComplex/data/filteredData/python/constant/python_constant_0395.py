import random

def main(n):
    # 生成测试数据：长度为 n 的两行，仅包含字符 '0' 和 '1'
    a = [random.choice(['0', '1']) for _ in range(n)]
    b = [random.choice(['0', '1']) for _ in range(n)]

    ans = 0
    for i in range(n):
        if a[i] == "0":
            ans += 1
            if i - 1 >= 0 and a[i] == b[i] == b[i - 1]:
                a[i] = b[i] = b[i - 1] = "X"
            elif i + 1 < n and b[i] == b[i + 1] == a[i + 1] == a[i]:
                a[i] = b[i] = a[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i] == b[i + 1]:
                a[i] = b[i] = b[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i + 1] == a[i + 1]:
                a[i] = b[i + 1] = a[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i] == a[i + 1]:
                a[i] = b[i] = a[i + 1] = "X"
            else:
                ans -= 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)