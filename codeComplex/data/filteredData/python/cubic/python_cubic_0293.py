import random

def main(n: int):
    # 这里用 n 控制每种颜色数量，示例：r = g = b = n
    r = g = b = n

    # 根据 n 生成测试数据（这里使用 1~100 的随机整数）
    random.seed(0)  # 固定随机种子，保证可复现
    R = [random.randint(1, 100) for _ in range(r)]
    G = [random.randint(1, 100) for _ in range(g)]
    B = [random.randint(1, 100) for _ in range(b)]

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
    print(result)


if __name__ == "__main__":
    # 示例：规模为 3
    main(3)