import random

def main(n):
    # 生成测试数据：T 组测试，每组长度为 n 的数组
    T = 1  # 可以按需修改为其他值
    print(f"T = {T}")
    for _ in range(T):
        # 生成长度为 n 的数组，元素为 1 到 10^9 之间的随机整数
        a = [random.randint(1, 10**9) for _ in range(n)]
        print("generated a:", a)

        # 原始逻辑
        a.sort()
        ans = min(len(a) - 2, max(a[-2] - 1, 0))
        print("answer:", ans)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)