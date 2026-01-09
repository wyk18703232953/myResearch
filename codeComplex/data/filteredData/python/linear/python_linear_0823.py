from math import *


def main(n):
    # 根据规模 n 生成测试数据：
    # 这里构造一个“有解”的 k，方式是先随机选一个 t (0 <= t < n)，
    # 再用程序的等价逻辑求出对应的 k。
    #
    # 原逻辑判断条件:
    #   s - (n - i - 1) == k 时输出 (n - i - 1)
    # 我们反推：给定要输出的答案 t = (n - i - 1)，则
    #   k = s - t
    #
    # 为简化，这里选择 t = n // 2（可以按需修改生成策略）。
    if n <= 1:
        # 规模太小直接返回 0
        # print(0)
        pass
        return

    target_t = n // 2  # 希望最终输出的值
    target_i = n - target_t - 1

    # 计算循环到 i = target_i 时的 s
    s = 1
    dob = 2
    if target_i >= 1:
        for i in range(1, target_i + 1):
            s += dob
            dob += 1

    k = s - target_t  # 构造的 k，使得在 i = target_i 时触发条件

    # 下面是原逻辑，只是用生成的 n, k
    s = 1
    dob = 2
    for i in range(1, n):
        s += dob
        dob += 1
        if s - (n - i - 1) == k:
            # print(n - i - 1)
            pass
            return
    # print(0)
    pass


# 示例调用
if __name__ == "__main__":
    # 你可以在这里修改 n 以测试不同规模
    main(10)