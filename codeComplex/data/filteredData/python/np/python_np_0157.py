import random

def main(n):
    # 生成测试数据
    # 约束范围可以按需调整
    l = random.randint(1, 50)
    r = random.randint(l, 100)  # 保证 r >= l
    x = random.randint(0, 20)   # 难度差下限
    diff = [random.randint(1, 50) for _ in range(n)]

    ans = 0

    # 遍历所有子集（排除空集）
    for mask in range(1, 1 << n):
        curr_sum = 0
        maxim = 0
        minim = 10**9

        for bit in range(n):
            if mask & (1 << bit):
                val = diff[bit]
                curr_sum += val
                if val > maxim:
                    maxim = val
                if val < minim:
                    minim = val

        if l <= curr_sum <= r and maxim - minim >= x:
            ans += 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可调整
    main(5)