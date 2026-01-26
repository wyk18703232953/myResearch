import collections

def generate_strings(n):
    # 保证 n >= 1
    if n <= 0:
        n = 1
    # 构造一个确定性的字符串 s，长度为 n
    s = "".join(chr(ord('a') + (i % 26)) for i in range(n))
    # 构造一个确定性的 t，为 s 的一种确定性“扰动”但字符频次相同
    # 这里做一次简单的循环右移，保证 Counter(s) == Counter(t)
    if n == 1:
        t = s

    else:
        shift = n // 2  # 确定性的偏移
        shift %= n
        t = s[shift:] + s[:shift]
    return s, t

def main(n):
    s, t = generate_strings(n)
    if collections.Counter(s) != collections.Counter(t):
        # print(-1)
        pass
        return
    sl = list(s)
    st = list(t)
    ans = []
    p = 0
    while sl:
        if sl[0] != st[0]:
            k = sl.index(st[0])
            ans.extend(list(range(k + p, p, -1)))
            sl.pop(k)
            st.pop(0)

        else:
            sl.pop(0)
            st.pop(0)
        p += 1
    # print(len(ans))
    pass

    if ans:
        # print(*ans)
        pass
if __name__ == "__main__":
    # 示例：以 n=10 作为输入规模
    main(10)