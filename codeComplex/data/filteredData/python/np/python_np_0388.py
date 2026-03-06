def main(n):
    # n controls both number of rows and columns: n x n matrix
    m = n
    if n <= 0:
        print(-1, -1)
        return

    # Deterministic matrix generation: l[i][j] = (i * 131 + j * 17) % 10**9
    l = [[(i * 131 + j * 17) % (10**9) for j in range(m)] for i in range(n)]

    pm = (1 << m) - 1

    from collections import defaultdict

    def find(x):
        s = set()
        d = defaultdict(int)
        for i in range(n):
            a_bits = []
            for j in range(m):
                if l[i][j] >= x:
                    a_bits.append('1')
                else:
                    a_bits.append('0')
            a_str = ''.join(a_bits)
            val = int(a_str, 2)
            d[val] = i
            s.add(val)
        s_list = list(s)
        for i in range(len(s_list)):
            for j in range(i, len(s_list)):
                if (s_list[i] | s_list[j]) == pm:
                    return [d[s_list[i]] + 1, d[s_list[j]] + 1]
        return [-1, -1]

    st = 0
    end = 10**9
    ans = (0, 0)
    while st <= end:
        mid = (st + end) // 2
        res = find(mid)
        if res[0] != -1:
            ans = tuple(res)
            st = mid + 1
        else:
            end = mid - 1

    print(ans[0], ans[1])


if __name__ == "__main__":
    main(5)