import random

def main(n):
    # 1. 生成测试数据
    # 题意：有 n 道题，每道题有一个难度值 c[i]
    # 这里生成 c 为 1~1000 的随机整数
    c = [random.randint(1, 1000) for _ in range(n)]
    
    # 生成 l, r, x，保证有意义：0 <= l <= r，x >= 0
    total_sum = sum(c)
    l = random.randint(0, max(0, total_sum - 1))
    r = random.randint(l, total_sum)
    x = random.randint(0, max(c) - min(c) if n > 1 else 0)

    # 2. 原逻辑
    res = 0
    for mask in range(1 << n):
        chosen = []
        for j in range(n):
            if mask & (1 << j):
                chosen.append(c[j])
        if len(chosen) >= 2 and l <= sum(chosen) <= r and (max(chosen) - min(chosen) >= x):
            res += 1

    print(res)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)