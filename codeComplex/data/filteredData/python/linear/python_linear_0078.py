import random

def main(n: int):
    # 生成规模为 n 的测试数据：
    # first 的长度为 n
    # second 的长度为 n + random_offset（保证 second 至少与 first 一样长）
    if n <= 0:
        return

    # first 和 second 都是由 '0' 和 '1' 构成的字符串
    first_len = n
    second_len = n + random.randint(0, n)  # 保证 second_len >= first_len

    first_str = ''.join(random.choice('01') for _ in range(first_len))
    second_str = ''.join(random.choice('01') for _ in range(second_len))

    first = [int(i) for i in first_str]
    second = [int(i) for i in second_str]

    # 原始逻辑
    pref_dists = [
        [0] + [int(0 != c) for c in second],
        [0] + [int(1 != c) for c in second]
    ]
    for i in range(1, len(second) + 1):
        pref_dists[0][i] += pref_dists[0][i - 1]
        pref_dists[1][i] += pref_dists[1][i - 1]

    total = 0
    for i, c in enumerate(first):
        end = len(second) - (len(first) - i)
        total += pref_dists[c][end + 1] - pref_dists[c][i]

    # 输出生成的测试数据和结果，便于验证
    print(first_str)
    print(second_str)
    print(total)


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改或在外部调用 main(n)
    main(5)