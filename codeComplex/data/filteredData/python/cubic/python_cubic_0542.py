from random import randint

def main(n):
    """
    n: 控制测试数据规模（大致表示 a 的位数上限）
    逻辑：给定整数 a，寻找由 a 的数字重排后形成的、不超过 b 的最大数。
    这里为了自洽，生成测试数据时令 b = a 的一个随机排列形成的整数，
    再在程序中求出答案。
    """
    # 生成测试数据
    # 控制 a 的位数在 [1, n] 之间
    length = max(1, n)
    # 生成 length 位的随机整数 a（首位不为 0）
    first_digit = randint(1, 9)
    other_digits = [randint(0, 9) for _ in range(length - 1)]
    digits = [first_digit] + other_digits
    a = int("".join(map(str, digits)))

    # 生成 b：把 a 的数字随机打乱一次
    from random import shuffle
    perm_digits = digits[:]
    shuffle(perm_digits)
    b = int("".join(map(str, perm_digits)))

    # 原逻辑开始：给定 a, b 计算答案
    arr = list(str(a))
    arr = sorted(arr)
    ans = ''

    while arr:
        for i in range(len(arr) - 1, -1, -1):
            x = ans + arr[i]

            # 把当前选择的位放在前面，其他位按原顺序拼接
            for j in arr[:i]:
                x += j
            for j in arr[i + 1:]:
                x += j

            if int(x) <= b:
                ans += arr[i]
                arr.pop(i)
                break

    print("a =", a)
    print("b =", b)
    print("answer =", ans)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)