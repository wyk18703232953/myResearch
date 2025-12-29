import random
from bisect import bisect_right

def main(n):
    # 生成测试数据
    # 约定：k 在 [0, 10^9] 内，a_i 在 [0, 10^9] 内
    k = random.randint(0, 10**9)
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 原逻辑
    a = sorted(a) + [10**9]
    ans = n

    for x in a[:-1]:
        if a[bisect_right(a, x)] <= x + k:
            ans -= 1

    print(ans)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需调整
    main(10)