import random

def main(n: int):
    # 生成测试数据
    # d 在 1 到 n 之间取值
    d = random.randint(1, max(1, n))
    # 生成 n 个整数，范围自定，这里在 [0, 10*n] 内
    lst = [random.randint(0, 10 * n) for _ in range(n)]

    # 原始逻辑
    lst.sort()
    Ans = 2
    for i in range(1, n):
        if lst[i] - lst[i - 1] > 2 * d:
            Ans += 2
        elif lst[i] - lst[i - 1] == 2 * d:
            Ans += 1
    print(Ans)

if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)