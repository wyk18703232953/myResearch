from itertools import chain, combinations
from random import randint


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def main(n):
    # 根据规模 n 生成测试数据
    # n: 元素个数
    # 生成难度等级参数
    l = randint(1, 10)
    r = randint(l, l + 10 * n)  # 保证 r >= l
    x = randint(0, 10)

    # 生成 n 个随机整数
    ll = [randint(1, 20) for _ in range(n)]

    subsets = powerset(ll)
    res = 0
    for subset in subsets:
        if (
            len(subset) >= 2
            and l <= sum(subset) <= r
            and max(subset) - min(subset) >= x
        ):
            res += 1
    print(res)


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)