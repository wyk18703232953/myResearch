# -*- coding:utf-8 -*-

def steps(start, target):
    ans = 0
    for i, v in enumerate(start):
        u = target[i]
        if v != u:
            for j in range(i + 1, len(start)):
                a, b = start[j], target[j]
                if a != b and a == u:
                    start[i], start[j] = start[j], start[i]
                    break
            ans += 1
    return ans


def solve(seq):
    hc = seq.count('H')
    tc = len(seq) - hc
    ans = float('inf')
    for i in range(tc + 1):
        s = ['T'] * i + ['H'] * hc + ['T'] * (tc - i)
        ans = min(steps(seq.copy(), s), ans)
    for i in range(hc + 1):
        s = ['H'] * i + ['T'] * tc + ['H'] * (hc - i)
        ans = min(steps(seq.copy(), s), ans)
    return ans


def main(n):
    # 生成长度为 n 的测试数据，元素为 'H' 和 'T'
    # 简单策略：前半部分 'H'，后半部分 'T'
    seq = ['H'] * (n // 2) + ['T'] * (n - n // 2)
    # 也可以进行一个简单的打乱，让测试稍微多样化
    if n > 1:
        # 交换首尾作为轻微扰动
        seq[0], seq[-1] = seq[-1], seq[0]
    print(solve(seq))


if __name__ == "__main__":
    # 示例：n = 10
    main(10)