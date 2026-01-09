def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def main(n):
    # 解释原程序输入结构：
    # 第一行: n, r
    # 第二行: n 个整数 a[i]
    #
    # 这里将参数 n 作为“圆的个数”，即原程序中的 n
    # r 设为一个与规模无关的固定值，保证确定性
    if n <= 0:
        return

    r = 10  # 固定半径，保持算法逻辑不变

    # 构造确定性的数组 a，长度为 n
    # 使用简单线性构造，避免随机性
    a = [i * 3 for i in range(n)]

    ans = []
    ans.append(r)
    for i in range(1, n):
        ymax = r
        for j in range(i):
            if abs(a[j] - a[i]) <= 2 * r:
                ymax = max(
                    ymax,
                    ans[j] + (4 * r * r - (a[i] - a[j]) ** 2) ** 0.5
                )
        ans.append(ymax)

    # 保持与原程序相同的输出形式
    # print(*ans)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小进行实验
    main(10)