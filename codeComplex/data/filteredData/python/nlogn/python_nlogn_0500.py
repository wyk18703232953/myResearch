import random

def main(n):
    # 生成测试数据
    # 约束：最终必然可行（su <= m）
    # a_i, b_i 为正整数，规模、范围可按需调整
    a_list = []
    b_list = []
    sun = 0  # sum of a
    su = 0   # sum of b

    for _ in range(n):
        a = random.randint(1, 100)
        b = random.randint(1, a)  # 保证 a >= b，方便构造 su <= m
        a_list.append(a)
        b_list.append(b)
        sun += a
        su += b

    # 构造 m，使得 su <= m <= sun，且通常需要做压缩操作
    # 这里令 m 在 [su, sun] 范围内随机
    if su > sun:
        # 理论上不会发生，因为 b <= a
        m = sun
    else:
        m = random.randint(su, sun)

    # 原逻辑开始
    ans = 0
    dif = []
    for a, b in zip(a_list, b_list):
        dif.append(a - b)

    if su > m:
        print(-1)
    elif sun == m:
        print(0)
    else:
        dif.sort()
        j = n - 1
        while sun > m and j >= 0:
            sun -= dif[j]
            ans += 1
            j -= 1
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)