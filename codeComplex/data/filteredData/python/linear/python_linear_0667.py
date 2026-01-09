def main(n):
    # 确定性生成测试数据
    # n 作为数组长度和字符串长度
    if n <= 0:
        # print(0)
        pass
        return

    a = [(i * 3 + 1) % 10 + 1 for i in range(n)]  # 数组元素在 1..10 内循环
    chars = ['W', 'G', 'L']
    b = ''.join(chars[i % 3] for i in range(n))

    sol = 0
    e = 0
    big = 0
    g = 0
    for i in range(n):
        if b[i] == "W":
            big = 1
            sol += 3 * a[i]
            e += a[i]
        if b[i] == "G":
            sol += 5 * a[i]
            e += a[i]
            g += 2 * a[i]
        if b[i] == "L":
            sol += a[i]
            e -= a[i]
            if e < 0:
                if big:
                    sol -= 3 * e

                else:
                    sol -= 5 * e
                e = 0
        g = min(g, e)
    if e:
        sol -= 2 * g
        sol -= (e - g)

    # print(int(sol))
    pass
if __name__ == "__main__":
    # 示例：规模为 10 的调用
    main(10)