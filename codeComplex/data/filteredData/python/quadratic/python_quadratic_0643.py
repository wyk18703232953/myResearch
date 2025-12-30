import random

def main(n: int) -> int:
    # 生成测试数据：n 个随机正整数
    # 可根据需要调整数据范围
    a = [random.randint(1, 10 * n) for _ in range(n)]

    a.sort()
    ans = 0
    u = [0] * (n + 1)
    for i in range(n):
        if u[i] == 0:
            ans += 1
        for j in range(i, n):
            if a[j] % a[i] == 0:
                u[j] = 1
    print(ans)
    return ans

# 示例调用
if __name__ == "__main__":
    main(10)