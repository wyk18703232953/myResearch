import collections

def transform_string(s, t):
    if collections.Counter(s) != collections.Counter(t):
        return -1, []

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
    return len(ans), ans

def generate_strings(n):
    if n <= 0:
        return "", ""
    base = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = "".join(base)
    # Deterministic transformation of s to t:
    # rotate left by k where k = n // 3, then reverse whole string
    k = n // 3
    if k > 0:
        rotated = s[k:] + s[:k]

    else:
        rotated = s
    t = rotated[::-1]
    return s, t

def main(n):
    s, t = generate_strings(n)
    res, seq = transform_string(s, t)
    # print(res)
    pass

    if res != -1 and seq:
        # print(*seq)
        pass
if __name__ == "__main__":
    main(10)