def main(n: int):
    # 生成测试数据：让 a = n（规模），k 取一个相对合理的值，比如 a 的 1/10，至少为 1
    a = n
    k = max(1, a // 10)

    # 原逻辑开始
    p = []
    for x in range(2, a + 1):
        for d in range(2, int(x ** 0.5) + 1):
            if x % d == 0:
                break

        else:
            p.append(x)

    c = 0
    for i in range(0, len(p) - 1):
        s = p[i] + p[i + 1] + 1
        for d in range(2, int(s ** 0.5) + 1):
            if s % d == 0:
                break

        else:
            if s <= a:
                c += 1

    if c >= k:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例：规模 n = 50
    main(50)