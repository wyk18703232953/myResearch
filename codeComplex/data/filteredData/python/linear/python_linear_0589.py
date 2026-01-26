from sys import stdout

mod = 1000000007

def build_data(n):
    if n < 1:
        n = 1
    q = n
    # 生成长度为 n 的 01 字符串，模式完全确定
    s = ''.join('1' if (i * 3 + 1) % 5 < 3 else '0' for i in range(n))
    queries = []
    for i in range(q):
        l = (i * 2) % n
        r = (i * 3 + 1) % n
        if l > r:
            l, r = r, l
        # 转为 1-based
        queries.append((l + 1, r + 1))
    return n, q, s, queries

def solve(n, q, s, queries):
    arr = []
    count = 0
    for ch in s:
        if ch == '1':
            count += 1
        arr.append(count)

    ansarr = []
    for x, y in queries:
        if x == 1:
            total1 = arr[y - 1]

        else:
            total1 = arr[y - 1] - arr[x - 2]
        total0 = (y - x + 1 - total1)
        length = y - x + 1
        ans = pow(2, length, mod) % mod
        ans = ((((ans % mod) - (pow(2, total0, mod) % mod)) % mod) + mod) % mod
        ansarr.append(ans)
    return ansarr

def main(n):
    n_val, q_val, s, queries = build_data(n)
    ansarr = solve(n_val, q_val, s, queries)
    stdout.write('\n'.join(map(str, ansarr)))

if __name__ == "__main__":
    main(10)