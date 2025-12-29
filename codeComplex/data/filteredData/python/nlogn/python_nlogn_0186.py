from collections import defaultdict
import random

def main(n: int) -> int:
    # 1. 生成规模为 n 的测试数据，这里生成 [-10^5, 10^5] 范围内的随机整数
    # 如有需要可根据实际题目调整数据生成逻辑
    a = [random.randint(-10**5, 10**5) for _ in range(n)]

    tot = 0
    for i in range(n):
        l = i
        r = n - i - 1
        tot += a[i] * l + -a[i] * r

    for_cnt = defaultdict(int)
    for i in range(n):
        fault = for_cnt[a[i] - 1] + for_cnt[a[i] + 1] + for_cnt[a[i]]
        tot -= a[i] * fault
        for_cnt[a[i]] += 1

    back_cnt = defaultdict(int)
    i = n - 1
    while i >= 0:
        fault = back_cnt[a[i] - 1] + back_cnt[a[i] + 1] + back_cnt[a[i]]
        tot -= -a[i] * fault
        back_cnt[a[i]] += 1
        i -= 1

    print(tot)
    return tot

if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)