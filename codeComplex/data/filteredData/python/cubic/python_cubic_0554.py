def search(current, digits, target, idx, bulk):
    if len(current) == len(target) and int(current) <= int(target):
        # print(current)
        pass
        raise SystemExit

    possibilities = [char for char in digits if bulk or (char <= target[idx] and char in digits)]

    if len(possibilities) == 0:
        return None

    for possible_digit in sorted(set(possibilities), reverse=True):
        tmp_digits = list(digits)
        tmp_digits.remove(possible_digit)
        next_bulk = bulk
        if not bulk:
            next_bulk = True if possible_digit != target[idx] else False
        search(current + possible_digit, tmp_digits, target, idx + 1, next_bulk)


def main(n):
    """
    n 为规模参数：
    - 用前 n 个不同数字（从 9,8,7,...往下）构造 digits
    - target 为一个长度为 n 的数字串（从 1,2,3,...起，循环到 9）
    """
    # 生成 digits：最大不超过 10 个不同数字
    m = min(n, 10)
    # digits 从 '9' 往下取 m 个
    all_digits_desc = [str(d) for d in range(9, -1, -1)]
    digits = sorted(all_digits_desc[:m], reverse=True)

    # 生成 target：长度为 n，按 '1','2',...,'9' 循环
    target_digits = [str((i % 9) + 1) for i in range(n)]
    target = "".join(target_digits)

    if len(digits) < len(target):
        # print(''.join(digits))
        pass
        return

    entries = [char for char in digits if char <= target[0]]

    for current in sorted(set(entries), reverse=True):
        tmp_digits = list(digits)
        tmp_digits.remove(current)
        bulk = True if current != target[0] else False
        try:
            search(current, tmp_digits, target, 1, bulk)
        except SystemExit:
            return


if __name__ == "__main__":
    # 示例：调用 main(5)，可按需修改 n
    main(5)