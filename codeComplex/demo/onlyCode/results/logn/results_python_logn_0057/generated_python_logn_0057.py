from math import log
import random

def main(n):
    # 生成测试数据：根据规模 n 的大小范围生成 l, r
    # 这里约定：当 n > 1 时，l, r 在 [0, 2^n - 1] 内
    if n <= 1:
        l, r = 0, 1
    else:
        upper = (1 << n) - 1
        l = random.randint(0, upper)
        r = random.randint(l, upper)  # 保证 l <= r

    # 原始逻辑开始
    # 需处理 l == 0 或 r == 0 的情况，否则 log(0, 2) 会报错
    if l == r:
        # 若区间只有一个数，答案为 0
        print(0)
        return

    # 避免 log(0)；若有 0，则将其视作 1 以确定对数上界
    l_for_log = max(l, 1)
    r_for_log = max(r, 1)

    i = int(max(log(l_for_log, 2), log(r_for_log, 2)))
    while ((1 << i) & l) == ((1 << i) & r):
        i -= 1
        if i == -1:
            break
    i += 1
    print((1 << i) - 1)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)