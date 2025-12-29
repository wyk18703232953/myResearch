import random

def main(n: int):
    # 生成测试数据：t组测试，每组规模为n
    t = 5  # 可按需调整测试组数
    print(f"t = {t}")
    for _ in range(t):
        # 生成一组长度为 n 的随机数组
        # 保证 n >= 2 才有意义，否则跳过
        if n < 2:
            print("n 必须至少为 2")
            return

        # 这里生成 1 到 10^9 之间的随机整数
        arr = [random.randint(1, 10**9) for _ in range(n)]
        print(f"n = {n}")
        print("arr =", " ".join(map(str, arr)))

        arr.sort()
        a = arr[-2]
        ans = min(a - 1, n - 2)
        print("answer =", ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)