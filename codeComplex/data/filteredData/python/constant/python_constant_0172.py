import random

def main(n):
    # 1. 生成测试数据：根据规模 n 生成 (l, r)
    #   这里简单设计为：
    #   - 随机选择一个起点 l
    #   - 确保 r - l 的范围与规模 n 有关，例如在 [0, n] 内
    #   - 这样可以覆盖 r-l<2 和 r-l>=2 的情况
    if n <= 0:
        # 规模非法时，直接返回不做任何事
        return

    # 为了更稳定，保证有一部分测试是有解的：
    # 其中一半情况强制生成 r-l>=2，另一半随机
    if random.random() < 0.5:
        # 强制生成有解的情况
        l = random.randint(1, 10 * n)
        r = l + random.randint(2, n + 2)  # 至少间隔2
    else:
        # 随机生成，可能有解也可能无解
        l = random.randint(1, 10 * n)
        r = l + random.randint(0, n)

    # 2. 原始逻辑
    if l % 2:
        l += 1
    if r - l < 2:
        print(-1)
    else:
        print(l, l + 1, l + 2)


if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n
    main(10)