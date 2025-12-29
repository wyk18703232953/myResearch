import random

def main(n):
    # 1. 生成测试数据
    # 参数生成策略（可按需要调整）
    # 保证 T >= 1，且数组元素在 [1, T] 范围内，避免原程序中 for i in range(1, T) 出现问题
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    T = random.randint(1, 10)

    arr = [random.randint(1, T) for _ in range(n)]

    # 2. 原始逻辑
    Tcnt = arr.count(T)
    l = n - Tcnt  # （原程序中未使用，保留以保持结构一致）
    ans = 0
    a1 = 0

    for i in range(1, T):
        for j in range(n):
            if arr[j] <= i:
                a1 += 1
        ans += a1 * c
        a1 = 0

    b1 = 0
    for i in range(n):
        b1 = a - ((T - arr[i]) * b)
        if b1 <= 0:
            ans += b1
        else:
            ans += b1

    ans1 = n * a
    print(max(ans, ans1))


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)