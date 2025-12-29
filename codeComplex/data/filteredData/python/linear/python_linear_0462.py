def main(n):
    """
    生成长度为 n 的测试字符串 s（由 'b' 和 'w' 组成），
    然后执行原逻辑并返回结果。
    这里将 s 设为交替的 'b' 和 'w'，长度为 n。
    """
    # 生成测试数据：长度为 n 的 'b'、'w' 交替串
    # 示例：n=5 -> "bwbwb"
    s_input = ''.join('b' if i % 2 == 0 else 'w' for i in range(n))

    # 原逻辑开始
    s = 2 * s_input + "333"
    le = (len(s) - 3) // 2
    a = []
    for ch in s:
        if ch == 'b':
            a.append(0)
        if ch == 'w':
            a.append(1)
        if ch == '3':
            a.append(3)

    pehla = [0, 1] * len(s)
    doosra = [1, 0] * len(s)

    k = [0] * len(s)
    for i in range(len(s)):
        if a[i] == pehla[i]:
            k[i] = 1

    ans = 0
    t = 0
    for v in k:
        if v == 1:
            t += 1
        else:
            ans = max(ans, t)
            t = 0

    k = [0] * len(s)
    for i in range(len(s)):
        if a[i] == doosra[i]:
            k[i] = 1

    t = 0
    for v in k:
        if v == 1:
            t += 1
        else:
            ans = max(ans, t)
            t = 0

    return min(le, ans)


# 示例调用
if __name__ == "__main__":
    # 可根据需要修改 n
    result = main(10)
    print(result)