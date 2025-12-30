import random
import string


def maxlen_from_string(s: str) -> int:
    """
    返回字符串 s 中出现至少两次的子串的最大长度。
    """
    maxi = 0
    # 枚举起始位置
    for x in range(len(s)):
        substring = ""
        # 逐字符扩展子串
        for y in s[x:]:
            substring += y
            # 在 s[x:] 中，若该子串的第一次出现位置和最后一次出现位置不同
            # 则说明出现次数 >= 2
            subrange = s[x:]
            if subrange.rfind(substring) != subrange.find(substring):
                maxi = max(maxi, len(substring))
                # 原代码这里是 continue，相当于只是跳到下一个 y
                # 不会 break，因此保持原逻辑不变
                continue
    return maxi


def main(n: int) -> None:
    """
    n 为规模参数，用于生成测试数据并执行原逻辑。

    这里将 n 视为要生成的随机字符串长度。
    字符串由小写字母组成。
    """
    # 生成长度为 n 的随机字符串，字符集为小写字母
    test_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 打印以便看到测试数据（如果不需要可以注释掉）
    # print(test_string)

    result = maxlen_from_string(test_string)
    print(result)


if __name__ == "__main__":
    # 示例：以 n = 20 运行
    main(20)