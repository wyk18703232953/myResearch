from itertools import chain, combinations
import random

def powerset(iterable):
    xs = list(iterable)
    return list(chain.from_iterable(combinations(xs, n) for n in range(2, len(xs) + 1)))

def main(n):
    # 生成测试参数
    # sett 为 n 个随机整数，范围在 1~1000 之间
    sett = [random.randint(1, 1000) for _ in range(n)]
    sett.sort()

    # 生成约束 l, r, x
    total_sum = sum(sett)
    l = random.randint(0, total_sum // 2 if total_sum > 0 else 0)
    r = random.randint(l, total_sum if total_sum > 0 else l)
    x = random.randint(0, max(sett) - min(sett) if n > 1 else 0)

    psett = powerset(sett)
    count = 0
    for i in psett:
        k = sorted(i)
        j = sum(k)
        if l <= j <= r and k[-1] - k[0] >= x:
            count += 1

    print(count)

if __name__ == "__main__":
    # 示例：调用 main，n 为规模（子集元素个数的上限）
    main(10)