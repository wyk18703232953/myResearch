import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成一个区间 [l, r]
    # 这里令 r 在 [0, 2^n - 1] 范围内，l 在 [0, r] 范围内
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        r = random.randint(0, max_val)
        l = random.randint(0, r)

    # 原逻辑
    ans = 0
    for i in range(63, -1, -1):
        if (r & (1 << i)) > 0 and (l & (1 << i)) == 0:
            ans = (1 << (i + 1)) - 1
            break

    print(ans)

if __name__ == "__main__":
    # 示例：用规模 n=10 运行
    main(10)