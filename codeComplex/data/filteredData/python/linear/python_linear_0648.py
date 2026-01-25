from __future__ import division
from collections import Counter

def main(n):
    # 固定 c，使用确定性规则生成长度为 n 的序列 a
    # 规则：a[i] = (i % 5) + 1，c = 3
    c = 3
    a = [(i % 5) + 1 for i in range(n)]

    tel = Counter()
    target_count_last = Counter()
    targets = 0
    best = 0

    for num in a:
        if num == c:
            targets += 1
        else:
            since_last = targets - target_count_last[num]
            target_count_last[num] = targets
            tel[num] = max(0, tel[num] - since_last)
            tel[num] += 1
            best = max(best, tel[num])

    result = targets + best
    print(result)
    return result


if __name__ == "__main__":
    main(10)