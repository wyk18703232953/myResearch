import random

def main(n: int):
    # 这里将 m 规模与 n 关联，例如 m = min(8, n)，避免 2^m 过大；可按需调整
    m = min(8, max(1, n))

    # 生成测试数据：n 行，每行 m 个整数，范围 0 ~ 10^9
    l = [[random.randint(0, 10**9) for _ in range(m)] for _ in range(n)]

    left = 0
    right = 10**9 + 1
    ans = (1, 1)  # 预设一个合法形式的答案，防止极端情况下未赋值

    while left < right:
        mid = (left + right) // 2
        dicta = {}
        for i in range(n):
            mask = 0
            for j in range(m):
                mask <<= 1
                if l[i][j] >= mid:
                    mask += 1
            dicta[mask] = i

        ok = False
        full_mask = (1 << m) - 1
        for mi in dicta:
            if ok:
                break
            for mj in dicta:
                if mi | mj == full_mask:
                    ok = True
                    ans = (dicta[mi] + 1, dicta[mj] + 1)
                    break

        if ok:
            left = mid + 1
        else:
            right = mid

    print(*ans)


if __name__ == "__main__":
    # 示例：运行 main，规模 n 可在这里调整
    main(5)