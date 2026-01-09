# Problem G - transformed version without input(), with main(n)

MY_MOD = 10 ** 9 + 7


def solve(num_str: str) -> int:
    num_list = [int(ch) for ch in num_str]
    myMod = MY_MOD
    length = len(num_list)

    # f[i] = 111...1 (i digits) mod myMod
    # t[i] = 10^i mod myMod
    f = [0] * (length + 1)
    t = [1] * (length + 1)
    for i in range(length):
        f[i + 1] = (f[i] * 10 + 1) % myMod
        t[i + 1] = (t[i] * 10) % myMod

    ans = 0
    for i in range(1, 10):
        dp = [0] * (length + 1)
        for j in range(length):
            dp[j + 1] = (dp[j] * i + (10 - i) * (dp[j] * 10 + t[j])) % myMod
        c = 0
        ctr = 0
        for k in num_list:
            z = min(i, k)
            o = k - z
            ans += o * (dp[length - 1 - ctr] * t[c + 1] + f[c + 1] * t[length - 1 - ctr]) % myMod
            ans += z * (dp[length - 1 - ctr] * t[c] + f[c] * t[length - 1 - ctr]) % myMod
            ans %= myMod
            c += k >= i
            ctr += 1
        ans += f[c]
        if ans >= myMod:
            ans -= myMod
    return ans


def main(n: int) -> None:
    """
    生成长度为 n 的测试数据，并输出原算法对应结果。
    测试数据规则：构造由数字 '1' 重复 n 次的字符串。
    如 n=5 -> "11111"
    """
    if n <= 0:
        # 对于非正 n，视为空数字串，这里直接输出 0
        # print(0)
        pass
        return

    num_str = "1" * n
    ans = solve(num_str)
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：将这里的 n 改成需要的规模后直接运行
    main(5)