import random

def main(n: int):
    # 生成测试数据：a 为 1..n 的随机排列，b 为 1..10^6 的随机权值
    a = list(range(1, n + 1))
    random.shuffle(a)
    b = [random.randint(1, 10**6) for _ in range(n)]

    ans = float('inf')
    for i in range(1, n - 1):
        bef = aft = float('inf')
        for j in range(i):
            if a[j] < a[i]:
                bef = min(bef, b[j])
        for j in range(i, n):
            if a[i] < a[j]:
                aft = min(aft, b[j])
        ans = min(ans, b[i] + bef + aft)

    print(-1 if ans > 10**9 else ans)


if __name__ == "__main__":
    # 示例：可根据需要修改规模
    main(5)