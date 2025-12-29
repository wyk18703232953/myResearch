import random

def main(n):
    # 1. 生成测试数据：构造一个长度为 n 的数组 a[1..n]
    #    这里示例使用随机整数，你可以按需要修改生成规则
    a = [random.randint(0, 1000) for _ in range(n)]

    # 2. 将原先交互的 ask(x) 改为本地查询
    #    下标从 1 开始，按题意对 n 取模
    def ask(x):
        # 原代码中 x 在 [1..n]，且会用 (mid+t-1)%n+1 形式访问
        # 这里保持相同的 1-based 逻辑
        x = (x - 1) % n  # 转为 0-based
        return a[x]

    t = n // 2
    if t & 1:
        # 原代码输出 "! -1" 并退出
        print("! -1")
        return

    l = 1
    r = n
    while l < r:
        mid = (l + r) >> 1
        if ask(mid) >= ask((mid + t - 1) % n + 1):
            r = mid
        else:
            l = mid + 1

    # 输出结果下标和测试数据，方便验证
    print("! {}".format(l))
    # 如果只想保留原样输出，可去掉下面这行
    # print("array:", a)

if __name__ == "__main__":
    # 示例：规模 n 可在此指定或在其它地方调用 main(n)
    main(10)