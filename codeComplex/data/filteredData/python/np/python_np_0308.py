mod = 998244353

def main(n):
    # 这里根据规模 n 生成一个测试用的 k
    # 原程序中要求 key[1] 最终等于 k，且中间有若干 +-1 或 +-2 的变化
    # 为了保证有一定概率产生非零结果，这里简单取 k = n
    k = n

    NEXT = {(0, 1): 2, (1, 2): 2}  # 初始状态

    for i in range(1, n):
        NOW = NEXT
        NEXT = dict()
        for key in NOW:
            state, val = key

            if state == 0:
                if k - (n - i) * 2 <= val <= k:
                    NEXT[key] = (NEXT.get(key, 0) + NOW[key]) % mod
                if k - (n - i) * 2 < val + 1 <= k:
                    NEXT[(0, val + 1)] = (NEXT.get((0, val + 1), 0) + NOW[key]) % mod
                    NEXT[(1, val + 1)] = (NEXT.get((1, val + 1), 0) + NOW[key] * 2) % mod
            else:
                if k - (n - i) * 2 <= val <= k:
                    NEXT[key] = (NEXT.get(key, 0) + NOW[key]) % mod
                    NEXT[(0, val)] = (NEXT.get((0, val), 0) + NOW[key] * 2) % mod

                if k - (n - i) * 2 < val + 2 <= k:
                    NEXT[(1, val + 2)] = (NEXT.get((1, val + 2), 0) + NOW[key]) % mod

    ANS = 0
    for key in NEXT:
        if key[1] == k:
            ANS = (ANS + NEXT[key]) % mod

    print(ANS)


if __name__ == "__main__":
    # 可以在此处修改 n 的值进行测试
    main(5)