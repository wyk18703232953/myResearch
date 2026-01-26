def main(n):
    # 由 n 确定性生成 a
    # 这里生成一个长度为 n 的“数字数组” b，然后将其拼成十进制整数 a
    # 生成规则完全确定：第 j 位为 (j % 10) + 1（避免出现 0，使得逻辑更有意义）
    if n <= 0:
        # print("NO")
        pass
        return

    b = [((j % 10) + 1) for j in range(n)]
    a = 0
    for digit in b:
        a = a * 10 + digit

    # 以下为原程序逻辑，使用生成的 a 和 n
    s = 0
    t = a
    b = []
    for _ in range(n):
        s += t % 10
        b.append(t % 10)
        t //= 10
    b.reverse()

    i = 2
    ans = False
    if s == 0:
        ans = True
    while i <= s:
        if s % i != 0:
            i += 1
            continue
        l = s // i
        c = 0
        su = 0
        for j in range(n):
            if su > l:
                break

            else:
                su += b[j]
                if su == l:
                    su = 0
                    c += 1
        if c == i:
            ans = True
        i += 1
    if ans:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用，可按需修改 n 进行规模实验
    main(10)