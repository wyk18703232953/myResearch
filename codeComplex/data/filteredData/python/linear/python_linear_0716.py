import random

def main(n):
    # 生成测试数据：n 个随机正整数，这里取 1~10^6 作为范围
    a = [random.randint(1, 10**6) for _ in range(n)]

    ans = float('inf')
    for i in range(n):
        denom = max(i, n - i - 1)
        # 当 denom 为 0 时跳过，否则会出现除以 0
        if denom == 0:
            continue
        ans = min(ans, a[i] // denom)

    print(ans)

if __name__ == "__main__":
    # 示例执行：可根据需要修改 n 的大小
    main(10)