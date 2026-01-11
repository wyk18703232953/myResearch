def main(n):
    # 确定性生成权重数组 w，长度为 n
    w = [i * 2 + 1 for i in range(n)]

    # 生成操作序列 ent，长度为 2n，包含恰好 n 个 '0' 和 n 个 '1'
    # 规则：前 n 个为 '0'，后 n 个为 '1'，保证合法栈操作
    ent = "0" * n + "1" * n

    mp = {w[i]: i + 1 for i in range(n)}
    sorted(mp)
    w.sort()
    ptr = 0
    stk = []
    output = []

    for i in range(2 * n):
        if ent[i] == "0":
            output.append(str(mp[w[ptr]]))
            stk.append(mp[w[ptr]])
            ptr += 1

        else:
            output.append(str(stk.pop()))
    # print(" ".join(output))
    pass
if __name__ == "__main__":
    main(5)