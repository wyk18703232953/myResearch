def main(n):
    """
    根据规模 n 生成测试字符串 s 和整数 k，
    然后执行原程序逻辑并返回结果字符串。
    """
    # 生成测试数据：
    # 长度约为 n 的字符串，由周期性和非周期性部分组成，便于测试算法
    if n <= 0:
        n = 1
    base = "abc"
    k = max(1, n // 3)  # 让 k 和 n 有一定关系但不太大

    # 周期部分长度 p
    p = max(1, n // 5)
    period = (base * ((p // len(base)) + 1))[:p]
    # 非周期尾部
    tail_len = max(1, n - p)
    tail = (base[::-1] * ((tail_len // len(base)) + 1))[:tail_len]

    s = (period + tail)[:n]

    # 原始逻辑开始：-------------------------------------------------
    # 在原代码中，n 未被使用，仅 s 和 k 被使用
    # n , k = tup()
    # s , i = S() , 1

    i = 1
    # 找到最小 i，使得 s[i:] == s[:-i]，即找到最小循环平移
    while s[i:] != s[:-i]:
        i += 1
        if i >= len(s):  # 保险防护：如果找不到（理论上一定能找到），避免无限循环
            i = len(s)
            break

    result = s[:i] * k + s[i:]
    return result


if __name__ == "__main__":
    # 简单示例运行，可按需修改 n
    n = 20
    # print(main(n))
    pass