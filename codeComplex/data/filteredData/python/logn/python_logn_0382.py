import random

def main(n):
    # 生成测试数据：一个长度为 n 的数组 a，内部可以根据需求调整生成方式
    # 这里使用 1..100 之间的随机整数
    a = [random.randint(1, 100) for _ in range(n)]

    # 被原程序 ask(x) 替代的函数：查询数组中第 x 个位置的值（1-based）
    def ask(x):
        return a[x - 1]

    t = n // 2
    if t & 1:
        # 原程序输出 -1 并退出
        print(-1)
        return

    l = 1
    r = n
    while l < r:
        mid = (l + r) >> 1
        # (mid + t - 1) % n + 1 为环状索引
        if ask(mid) >= ask((mid + t - 1) % n + 1):
            r = mid
        else:
            l = mid + 1

    # 原程序输出为"! l"，这里直接输出 l 和用于调试的数组 a
    print("answer index:", l)
    print("array:", a)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时由外部传入 n
    main(10)