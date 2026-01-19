import sys

def main(n):
    # Interpret n as both number of rows and columns for scalability
    if n <= 0:
        return

    m = n

    # Deterministically generate matrix a of size n x m
    # Use simple arithmetic, values in [0, 1_000_000_000]
    limit = 10**9
    a = [[(i * m + j) % (limit + 1) for j in range(m)] for i in range(n)]

    mi = -1
    ma = 10**9
    ans = []

    while mi < ma:
        mid = (mi + ma + 1) // 2
        masks = {}
        for i in range(n):
            currMask = 0
            for j in range(m):
                if a[i][j] >= mid:
                    currMask += 1 << j
            masks[currMask] = i
        req = (1 << m) - 1
        possible = 0
        for i_mask in masks:
            for j_mask in masks:
                if i_mask | j_mask == req:
                    possible = 1
                    ans = [masks[i_mask] + 1, masks[j_mask] + 1]
                    break
            if possible:
                break
        if possible:
            mi = mid
        else:
            ma = mid - 1

    if ans:
        print(*ans)
    else:
        print(-1, -1)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)