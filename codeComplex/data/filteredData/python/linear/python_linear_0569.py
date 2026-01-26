def main(n):
    if n <= 0:
        return

    # 构造一个确定性的树父节点数组 fa，根为 1
    # 对于 i>=2，父亲为 i//2，保证是一棵树且与 n 确定性对应
    fa = [0, 0]
    for i in range(2, n + 1):
        fa.append(i // 2)

    delta = [0] * (n + 1)
    suml = [0] * (n + 1)

    for i in range(n, 0, -1):
        if suml[i] == 0:
            suml[i] = 1
        delta[suml[i]] += 1
        suml[fa[i]] += suml[i]

    for i in range(1, n + 1):
        delta[i] += delta[i - 1]

    ans = 0
    out = []
    for i in range(1, n + 1):
        while delta[ans] < i:
            ans += 1
        out.append(str(ans))
    # print(" ".join(out))
    pass
    # print()
    pass
if __name__ == "__main__":
    # 示例：使用一个固定的 n 进行调用
    main(10)