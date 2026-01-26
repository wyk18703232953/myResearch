def main(n):
    if n <= 0:
        # print("")
        pass
        return

    # deterministic array generation based on n
    # example pattern: arr[i] = (i * 2 + 3) % (n + 5) + i // 2
    arr = [(i * 2 + 3) % (n + 5) + (i // 2) for i in range(n)]

    memo = [-1 for _ in range(n + 1)]

    def can_win(idx):
        if memo[idx] != -1:
            return memo[idx]
        res = False

        delta = arr[idx]
        # right
        nidx = idx + delta
        while nidx < n:
            if arr[nidx] > arr[idx] and not can_win(nidx):
                res = True
                break
            nidx += delta

        # left
        nidx = idx - delta
        while (not res) and nidx >= 0:
            if arr[nidx] > arr[idx] and not can_win(nidx):
                res = True
                break
            nidx -= delta

        memo[idx] = res
        return res

    ans = ['A' if can_win(i) else 'B' for i in range(n)]
    # print(''.join(ans))
    pass
if __name__ == "__main__":
    # example deterministic call
    main(10)