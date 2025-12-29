from functools import lru_cache
import random

M = mod = 998244353


def factors(n):
    return sorted(
        set(
            sum(
                ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
                [],
            )
        )
    )


def inv_mod(n):
    return pow(n, mod - 2, mod)


def main(n: int):
    """
    n: 位数规模（生成 a 的位数），b 则在 [0, 10^n - 1] 之间随机生成。
    """

    # 生成测试数据
    # a 为一个 n 位非负整数（首位不为 0，除非 n=1）
    if n <= 0:
        raise ValueError("n must be positive")

    digits_a = [random.randint(0, 9) for _ in range(n)]
    if n > 1 and digits_a[0] == 0:
        digits_a[0] = random.randint(1, 9)
    a_val = int("".join(str(d) for d in digits_a))

    # b 在 [0, 10^n - 1] 范围内随机
    max_b = 10**n - 1
    b_val = random.randint(0, max_b)

    a = a_val
    b = b_val

    # 原程序逻辑开始
    n_local = len(str(a))

    a_digits = [int(i) for i in str(a)]
    a_digits.sort()

    if len(str(b)) > n_local:
        # 直接输出 a 的降序排列
        print("".join(str(d) for d in sorted(a_digits, reverse=True)))
        return

    b_str = str(b)
    b_digits = [int(i) for i in b_str]

    def givemax(sa, sb):
        # 比较两个数字字符串，返回数值更大的那个（长度优先，其次字典序）
        if len(sa) > len(sb):
            return sa
        elif len(sb) > len(sa):
            return sb
        else:
            return max(sa, sb)

    @lru_cache(None)
    def dp(l, equal=1):
        # l: 还剩下的数字（tuple）
        # equal: 当前前缀是否仍与 b 的前缀相等（1 是，0 否）
        if len(l) == 1:
            if equal and l[0] > b_digits[-1]:
                return "-inf"
            return str(l[0])

        if not equal:
            # 已经严格小于，后面直接放最大的排列
            return "".join(str(e) for e in sorted(l, reverse=True))

        # equal == 1
        ans = ""
        l_list = list(l)
        curr = b_digits[n_local - len(l_list)]
        for i in range(len(l_list)):
            d = l_list[i]
            rest = tuple(l_list[:i] + l_list[i + 1 :])
            if d < curr:
                sub = dp(rest, 0)
                if sub != "-inf":
                    ans = givemax(ans, str(d) + sub)
            elif d == curr:
                sub = dp(rest, 1)
                if sub != "-inf":
                    ans = givemax(ans, str(d) + sub)
        if ans == "":
            return "-inf"
        return ans

    result = dp(tuple(a_digits), 1)
    print(result)


if __name__ == "__main__":
    # 示例：规模为 5
    main(5)