def main(n):
    visit = [0 for _ in range(n + 1)]
    res = []
    c = 0
    s, t = 0, 0

    def do(i):
        nonlocal c, s, t
        for j in range(i, n + 1, 2 * i):
            res.append(i)
            c += 1
            if c >= (n - 1) and n > 2:
                if s == 0:
                    s = j

                else:
                    t = j

    i = 1
    while i <= n:
        do(i)
        i = 2 * i

    if n > 2 and len(res) >= n:
        res[n - 1] = max(s, t)

    # 输出，与原程序一致：元素间空格，末尾有空格
    for x in res:
        # print(x, end=" ")
        pass

# 示例调用
if __name__ == "__main__":
    # 可自行修改 n 用于测试
    main(10)