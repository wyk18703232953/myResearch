def main(n):
    # Map n to sizes of R, G, B
    r = n
    g = n
    b = n

    # Deterministically generate R, G, B based on n
    R = [(i * 2 + 1) % (3 * n + 1) + 1 for i in range(r)]
    G = [(i * 3 + 2) % (3 * n + 1) + 1 for i in range(g)]
    B = [(i * 5 + 3) % (3 * n + 1) + 1 for i in range(b)]

    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)

    memo = [[[-1] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    def calc(ir, ig, ib):
        if memo[ir][ig][ib] != -1:
            return memo[ir][ig][ib]
        ans = 0
        if ir < r and ig < g:
            ans = max(ans, calc(ir + 1, ig + 1, ib) + R[ir] * G[ig])
        if ir < r and ib < b:
            ans = max(ans, calc(ir + 1, ig, ib + 1) + R[ir] * B[ib])
        if ig < g and ib < b:
            ans = max(ans, calc(ir, ig + 1, ib + 1) + G[ig] * B[ib])
        memo[ir][ig][ib] = ans
        return ans

    result = calc(0, 0, 0)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(3)