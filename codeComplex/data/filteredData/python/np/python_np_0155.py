import random

def main(n: int) -> None:
    # 随机生成测试数据
    # 题意：原程序中 n,l,r,x 由输入给出，这里用 n 控制规模
    # 根据 n 构造合理的 l, r, x 和数组 c
    random.seed(0)  # 固定随机种子，方便复现

    # 生成题目难度数组 c，范围可按题意自定
    c = [random.randint(1, 100) for _ in range(n)]

    # 生成 l, r, x，保证 1 <= l <= r，并且 x 不超过可能的最大差值
    total_sum = sum(c)
    l = random.randint(0, total_sum // 2)
    r = random.randint(l, total_sum)
    max_diff = max(c) - min(c) if n >= 2 else 0
    x = random.randint(0, max_diff) if max_diff > 0 else 0

    ans = 0
    # 枚举所有大小至少为 2 的子集
    for bit in range(2, 1 << n):
        probs = []
        t = 0
        for i in range(n):
            if bit & (1 << i):
                probs.append(c[i])
                t += c[i]

        a = min(probs)
        b = max(probs)

        if l <= t <= r and abs(a - b) >= x:
            ans += 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模可在此修改
    main(5)