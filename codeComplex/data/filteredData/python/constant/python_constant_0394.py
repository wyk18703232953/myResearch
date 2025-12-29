import random

def main(n: int):
    # 生成测试数据：长度为 n 的由 '0' 和 '1' 组成的两行
    a = [random.choice(['0', '1']) for _ in range(n)]
    b = [random.choice(['0', '1']) for _ in range(n)]

    # 为了和原代码行为一致，需要对 a, b 进行可变修改，因此复制一份局部变量
    a = a[:]  # list of chars
    b = b[:]

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
    # 示例：可在此处修改 n 进行简单测试
    main(10)