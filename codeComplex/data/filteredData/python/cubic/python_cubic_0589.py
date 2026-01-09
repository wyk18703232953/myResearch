def main(n):
    # Deterministically construct strings a and b from n
    # Let length of a be n (at least 1), and b be the decimal of n padded/truncated
    if n <= 0:
        n = 1
    # a: repeating pattern of digits 0..9
    a = ''.join(str(i % 10) for i in range(n))
    # b: decimal representation of n, padded/truncated to length <= len(a)
    b_raw = str(n)
    if len(b_raw) > len(a):
        b = b_raw[:len(a)]

    else:
        b = b_raw.zfill(len(b_raw))
    # Keep original logic
    if len(a) < len(b):
        # print(*sorted(a, reverse=True), sep='')
        pass
        return

    cnt = [0] * 10
    for x in a:
        cnt[int(x)] += 1

    def rec(res, digit, rem):
        if digit == len(b):
            return res
        if rem[int(b[digit])]:
            r = rem[:]
            r[int(b[digit])] -= 1
            x = rec(res + b[digit], digit + 1, r)
            if x:
                return x
        for d in range(int(b[digit]) - 1, -1, -1):
            if rem[d]:
                res += str(d)
                rem[d] -= 1
                suf = []
                for i in range(10):
                    suf += [str(i)] * rem[i]
                return res + ''.join(sorted(suf, reverse=True))
        return ''

    ans = rec('', 0, cnt[:])
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)