def solve(b, freq, i, n, res):
    global success
    if i == len(b):
        success = res

    else:
        success = 0
        move = 9
        while move >= 0 and success == 0:
            m = int(b[i])
            if freq[move] > 0 and res * 10 + move <= n * 10 + m:
                res = res * 10 + move
                n = n * 10 + m
                freq[move] -= 1
                if solve(b, freq, i + 1, n, res) == 0:
                    res //= 10
                    n //= 10
                    freq[move] += 1
            move -= 1
    return success

def main(n):
    global success
    # 构造 a 和 b，使得 len(a) = n 且 len(b) = n
    # a 为从 0 到 9 循环的数字序列
    # b 为从 9 到 0 反向循环的数字序列
    a = ''.join(str(i % 10) for i in range(n))
    b = ''.join(str((9 - i) % 10) for i in range(n))

    freq = [0] * 10
    v = []
    for x in a:
        d = int(x)
        v.append(d)
        freq[d] += 1
    v.sort()

    if len(b) > len(a):
        ans = 0
        m = 1
        for x in v:
            ans = x * m + ans
            m *= 10

    else:
        success = 0
        ans = solve(b, freq, 0, 0, 0)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)