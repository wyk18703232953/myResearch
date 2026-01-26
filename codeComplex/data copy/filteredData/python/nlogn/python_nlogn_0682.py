def main(n):
    # Interpret n as both N and M (sizes of b and g)
    N = n
    M = n

    # Deterministically generate b and g
    # b: increasing sequence starting from 1
    b = [i + 1 for i in range(N)]
    # g: offset sequence to create varied relations between max(b) and min(g)
    g = [i + (n // 2) for i in range(M)]

    if max(b) > min(g):
        ans = -1
    elif max(b) == min(g):
        ans = M * sum(b)
        maxi = max(b)
        for i in range(M):
            if maxi == g[i]:
                continue

            else:
                ans += g[i] - maxi

    else:
        ans = M * sum(b)
        b.sort(reverse=True)
        for i in range(M):
            if i == 0:
                # Handle edge case when N < 2
                if N > 1:
                    ans += g[i] - b[1]

                else:
                    ans += g[i] - b[0]

            else:
                ans += g[i] - b[0]
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)