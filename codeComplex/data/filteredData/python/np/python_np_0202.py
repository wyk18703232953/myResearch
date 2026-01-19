from itertools import combinations

def main(n):
    # n作为题目数量规模，构造确定性数据
    # 为保证有意义的范围，设置l, r, x基于n
    l = n
    r = 3 * n
    x = n // 3 + 1

    # 构造长度为n的确定性整数数组
    # a[i] = i+1
    a = [i + 1 for i in range(n)]

    c = []
    for i in range(2, n + 1):
        c += list(combinations(a, i))

    cnt = 0
    for t in c:
        m = min(t)
        M = max(t)
        s = sum(t)
        if M - m >= x and (l <= s <= r):
            cnt += 1

    print(cnt)
    return cnt

if __name__ == "__main__":
    main(8)