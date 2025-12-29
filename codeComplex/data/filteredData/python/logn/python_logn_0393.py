import random

def main(n):
    # 原程序一开始就检查 n 是否满足 n % 4 != 2
    # 若不满足则直接输出 -1
    if n % 4 == 2:
        print('!', -1)
        return

    # 生成测试数据：
    # 原交互式程序的语义是：给定一个隐藏数组/函数 a[i]，
    # 通过 qry(i) 询问单点值；qry2(i) 比较 i 与 i + n//2。
    #
    # 这里构造一个长度为 n 的数组 arr，用于模拟 qry。
    # 可以根据需要修改生成方式。
    arr = [random.randint(-10, 10) for _ in range(n)]

    # 若希望保证一定存在某个 i 满足 arr[i] == arr[i + n//2]，
    # 可以手动构造，这里演示一种构造方式：
    half = n // 2
    base = random.randint(-10, 10)
    pos = random.randint(0, half - 1)
    arr[pos] = base
    arr[pos + half] = base

    def qry(i):
        # 模拟原来的交互查询：返回 arr[i]
        return arr[i]

    def qry2(i):
        a = qry(i + n // 2) - qry(i)
        if a == 0:
            # 找到解时立即输出并结束
            print('!', i + 1)
            return None, True  # (差值, 是否结束)
        return a, False

    # 开始模拟原程序逻辑
    a, done = qry2(0)
    if done:
        return

    lb, rb = 1, n // 2 - 1
    while lb <= rb:
        mb = (lb + rb) // 2
        b, done = qry2(mb)
        if done:
            return
        if (a > 0) == (b > 0):
            lb = mb + 1
        else:
            rb = mb - 1

    # 若逻辑结束仍未找到（理论上不应发生，作为兜底）
    print('!', -1)


if __name__ == "__main__":
    # 示例：调用 main(8)
    main(8)