import random

def main(n: int):
    # 1. 根据 n 生成测试数据
    # m：初始重量，取一个较为中等的值
    m = random.randint(1_000, 10_000)

    # a, b：生成每个位置的参数，避免为 0
    # 为了避免除法过大振荡，取相对适中的范围
    a = [random.randint(1, 1000) for _ in range(n)]
    b = [random.randint(1, 1000) for _ in range(n)]

    # 2. 原算法逻辑（去掉 input()，封装在 main 中）
    low = 1.0
    high = 1_000_000_000.0
    ans = -1.0
    eps = 1e-6

    while low <= high:
        if high - low < eps:
            low = high
        mid = low + (high - low) / 2.0
        try_val = mid
        init_wt = m + try_val
        isPossible = True

        for i in range(n):
            req1 = init_wt / a[i]
            try_val -= req1
            if try_val <= 0:
                isPossible = False
                break
            j = (i + 1) % n
            init_wt -= req1
            req2 = init_wt / b[j]
            try_val -= req2
            if try_val < 0 or (i < n - 1 and try_val == 0):
                isPossible = False
                break
            init_wt -= req2

        if isPossible:
            ans = mid
            high = mid - eps
        else:
            low = mid + eps

    if ans == -1:
        isPossible = True
        try_val = 1_000_000_000.000001
        init_wt = m + try_val
        for i in range(n):
            req1 = init_wt / a[i]
            try_val -= req1
            if try_val <= 0:
                isPossible = False
                break
            j = (i + 1) % n
            init_wt -= req1
            req2 = init_wt / b[j]
            try_val -= req2
            if try_val < 0 or (i < n - 1 and try_val == 0):
                isPossible = False
                break
            init_wt -= req2
        if isPossible:
            ans = 1_000_000_000.0

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5) 运行一次
    main(5)