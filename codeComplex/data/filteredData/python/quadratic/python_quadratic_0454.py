import random

def main(n: int):
    # 生成测试数据：长度为 n 的正整数数组
    # 这里简单生成 1~n 范围内的随机整数，保证至少为 1
    random.seed(0)
    arr = [random.randint(1, n) for _ in range(n)]

    memo = [-1 for _ in range(n + 1)]

    def can_win(idx: int) -> bool:
        if memo[idx] != -1:
            return memo[idx]

        res = False
        delta = arr[idx]

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
    print(''.join(ans))


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)