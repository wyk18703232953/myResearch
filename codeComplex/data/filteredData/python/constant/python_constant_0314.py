import random

def main(n):
    # 根据规模 n 生成测试数据，这里生成 n 个 0~9 的随机整数
    k = [random.randint(0, 9) for _ in range(n)]
    a = k[:]  # 与原程序中 a 的初始含义保持一致

    lst = []
    for i in range(n):
        p = k[i] % n
        ans = 0
        # 构造旋转后的数组 a（原代码中在循环内重定义了 a）
        a = k[i+1:] + k[:i+1]
        a[-1] = 0
        base = int(k[i] // n)
        for j in range(n):
            if (a[j] + 1 + base) % 2 == 0 and j < p:
                ans += a[j] + 1 + base
            elif (a[j] + base) % 2 == 0 and j >= p:
                ans += a[j] + base
        lst.append(ans)

    print(max(lst))


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)