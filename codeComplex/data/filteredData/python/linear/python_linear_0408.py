def main(n):
    # 将 n 映射为问题规模
    # 第一个字符固定为 'a'，其余根据 n 生成
    k = n if n > 0 else 1

    def tonny(i):
        return ord(i) - 96

    # 生成确定性字符串 s，长度为 n+1，字符在 'a' 到 'z' 周期分布
    s_chars = []
    for i in range(n + 1):
        s_chars.append(chr(97 + (i % 26)))
    s = "".join(s_chars)

    a = sorted(s)
    a = list(map(tonny, a))
    a = sorted(list(set(a)))

    if not a or k <= 0:
        print(-1)
        return

    ans = [a.pop(0)]
    k -= 1
    for j in a:
        if j - ans[-1] > 1 and k > 0:
            k -= 1
            ans.append(j)
        if k == 0:
            break
    if k != 0:
        print(-1)
    else:
        print(sum(ans))


if __name__ == "__main__":
    main(10)