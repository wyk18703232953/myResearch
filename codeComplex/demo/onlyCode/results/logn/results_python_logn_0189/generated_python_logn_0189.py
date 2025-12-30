def main(n):
    # 按题意：原本是从输入读取 n, s，这里用 n 作为规模参数
    # 需要根据 n 生成测试数据 (n, s)
    # 这里约定一个简单方案：s 与 n 同阶，例如 s = n
    s = n

    r = 0
    v = min(n + 1, s + 19 * 9)
    for i in range(s, v):
        zz = f'{i}'
        sm = i
        for z in zz:
            sm -= int(z)
        if sm >= s:
            r += 1

    ans = r + n - v + 1
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(100000) 或按需修改 n
    main(100000)