import random

def main(n):
    # 规模参数：n 为行数；这里令 m 与 n 同量级，可根据需要调整
    m = max(1, n // 2)  # 示例：列数设为 n//2，至少为 1

    # 3. 根据 n 生成测试数据 a（n 行 m 列的矩阵）
    # 生成范围 [1, 1e9] 的随机整数
    a = [[random.randint(1, 10**9) for _ in range(m)] for _ in range(n)]

    left = 0
    right = 10**9 + 1
    ans = (0, 0)

    while left < right:
        mid = (left + right) // 2
        masks = {}
        for i in range(n):
            mask = 0
            for j in a[i]:
                mask <<= 1
                if j >= mid:
                    mask += 1
            masks[mask] = i
        ok = False
        full_mask = (1 << m) - 1
        for m1 in masks:
            for m2 in masks:
                if m1 | m2 == full_mask:
                    ok = True
                    ans = (masks[m1] + 1, masks[m2] + 1)
                    break
            if ok:
                break
        if ok:
            left = mid + 1
        else:
            right = mid

    # 输出结果
    print(ans[0], ans[1])

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(5)