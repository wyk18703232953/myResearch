def main(n):
    if n <= 0:
        # print("")
        pass
        return

    # 确定性构造输入数组：略有起伏的整数序列
    # 示例：arr[i] = (i * 3) % (n // 2 + 1) + i // 3
    base = max(1, n // 2 + 1)
    arr = [(i * 3) % base + i // 3 for i in range(n)]

    memo = [-1 for _ in range(n)]

    def can_win(idx):
        if memo[idx] != -1:
            return memo[idx]
        res = False

        delta = arr[idx]

        # 防止 delta 为 0 导致死循环，保持逻辑完整性
        if delta == 0:
            memo[idx] = False
            return False

        # 向右跳
        nidx = idx + delta
        while nidx < n:
            if arr[nidx] > arr[idx] and not can_win(nidx):
                res = True
                break
            nidx += delta

        # 向左跳
        nidx = idx - delta
        while not res and nidx >= 0:
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
    main(10)