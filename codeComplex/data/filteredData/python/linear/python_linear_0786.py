def is_winning_state(nims, n):
    keys = set(nims)
    counts = dict.fromkeys(keys, 0)
    for nim in nims:
        counts[nim] += 1
    if 0 in keys and counts[0] > 1:
        return True
    lose_count = 0
    for k in keys:
        if counts[k] > 2:
            return True
        if counts[k] > 1 and (k - 1) in keys and counts[k - 1] > 0:
            return True
        if counts[k] > 1:
            lose_count += 1
    if lose_count > 1:
        return True
    return False


def main(n):
    # 生成规模为 n 的测试数据：使用 0, 1, 2, ..., n-1
    # 可以根据需要修改生成策略
    nims = list(range(n))

    if is_winning_state(nims, n):
        print('cslnb')
    else:
        x = sum(nims) - (n * (n - 1)) // 2
        if x % 2 == 0:
            print('cslnb')
        else:
            print('sjfnb')


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改或由外部调用 main(n)
    main(5)