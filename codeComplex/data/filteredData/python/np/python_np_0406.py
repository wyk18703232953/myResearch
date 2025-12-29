import random

def main(n):
    # 生成测试数据
    # 设 M 为列数，这里根据需要可以调整为与 n 相关或固定
    # 为保持原算法复杂度特征，取 M 为较小常数，例如 5
    M = 5
    N = n  # 行数 = 规模 n

    # 生成 N 行、每行 M 个随机正整数
    # 为了让二分有意义，数值范围设置为 1~10^9
    L = [[random.randint(1, 10**9) for _ in range(M)] for _ in range(N)]

    maxi = max(max(t) for t in L) + 1
    mini, res = max((min(t), i) for i, t in enumerate(L))
    res = (res, res)
    BITMASK = (1 << M)

    while True:
        mid = (maxi + mini) // 2
        if mid == mini:
            break
        masks = [None] * BITMASK
        for i, t in enumerate(L):
            tmask = 0
            for v in t:
                tmask *= 2
                if v >= mid:
                    tmask += 1
            if masks[tmask] is not None:
                continue
            masks[tmask] = i
            for k in range(BITMASK):
                if masks[k] is not None and (k | tmask) == BITMASK - 1:
                    res = (masks[k], i)
                    mini = mid = min(max(a, b) for a, b in zip(L[res[0]], L[res[1]]))
                    break
            else:
                continue
            break
        else:
            maxi = mid

    # 输出结果（1-based index）
    print(res[0] + 1, res[1] + 1)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要修改
    main(10)