from random import randint

mod = int(1e9 + 7)


def solve_from_string(s: str) -> int:
    """
    原 solve() 的核心逻辑，但从字符串 s 计算答案并返回，而不是打印。
    s 为仅包含数字字符的字符串。
    """
    arr = list(map(int, s))
    d, s_sum, ans = {0}, 0, 0
    for x in arr:
        s_sum += x
        s_sum %= 3
        if s_sum in d:
            ans += 1
            s_sum = 0
            d = {0}
        d.add(s_sum)
    return ans


def main(n: int):
    """
    n 为规模参数，这里用来生成长度为 n 的随机数字串作为测试数据，
    然后调用原逻辑进行计算并打印结果。
    """
    # 生成测试数据：长度为 n 的随机数字串（不含前导限制）
    s = ''.join(str(randint(0, 9)) for _ in range(n))

    # 调用核心逻辑
    ans = solve_from_string(s)

    # 输出结果（仅保留原程序的核心输出）
    print(ans)


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)