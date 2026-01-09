def main(n):
    # n controls:
    #   c = 1 (fixed "special" value)
    #   sequence length = n
    #   sequence pattern is deterministic:
    #       position i (1-based):
    #           if i % 3 == 0 -> value is c
    #           else -> value is (i % (n + 1)) + 1  (ensures values in [1, n+1])
    c = 1
    cnt = [0] * 500005
    ans = 0

    # Generate deterministic sequence of length n
    seq = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            seq.append(c)

        else:
            seq.append((i % (n + 1)) + 1)

    for v in seq:
        if v == c:
            cnt[c] = cnt[c] + 1

        else:
            if cnt[v] < cnt[c]:
                cnt[v] = cnt[c]
            cnt[v] += 1
        ans = max(ans, cnt[v] - cnt[c])
    result = ans + cnt[c]
    # print(result)
    pass
if __name__ == "__main__":
    main(10)