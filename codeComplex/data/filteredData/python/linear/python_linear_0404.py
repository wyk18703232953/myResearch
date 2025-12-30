import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 原程序逻辑：先读一行（无用），再读 m，然后再读两行，共计 4 行输入。
    #
    # 实际有意义的部分：
    #   m：整数
    #   接下来两行的所有整数拼接后，以 a 为元素，计算 v *= a/(a-1)
    #
    # 下面根据 n 来构造：
    #   - m: 与 n 相关的正整数
    #   - 两行各有 n 个整数，每个整数 >= 2 避免除零
    # 可根据需要调整生成策略，这里选择简单且稳定的规则。

    # 生成 m
    m = max(1, n)  # 保证 m >= 1

    # 生成两行各 n 个整数（>=2）
    line1 = [random.randint(2, 10) for _ in range(n)]
    line2 = [random.randint(2, 10) for _ in range(n)]

    # 模拟原始代码逻辑
    v = m
    try:
        # 将两行拼接成原代码中的 (i() + ' ' + i())
        all_nums = line1 + line2
        for a in all_nums:
            v *= a / (a - 1)
    except Exception:
        v = m - 1

    # 输出与原程序一致的结果：print(v - m)
    print(v - m)

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(5)