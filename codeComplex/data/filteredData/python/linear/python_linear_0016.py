import random

def f(n: int) -> bool:
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True

def main(n: int) -> None:
    # 根据规模 n 生成测试数据：
    # n 保持为给定规模；k 随机设为 [1, n]（至少 1，至多 n）
    if n < 2:
        print("NO")
        return

    k = random.randint(1, max(1, n // 2))

    a = []
    x = 0
    for i in range(2, n + 1):
        if f(i):
            a.append(i)
    for i in range(len(a) - 2):
        if a[i] + a[i + 1] + 1 in a:
            x += 1
    if x >= k:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main，指定规模 n
    main(50)