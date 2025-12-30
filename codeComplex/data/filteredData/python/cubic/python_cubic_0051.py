import random
import string

def main(n: int):
    # 根据规模 n 生成测试字符串：
    # 生成一个长度为 n 的随机小写字母串
    s = ''.join(random.choices(string.ascii_lowercase, k=n))

    # 原始逻辑：寻找最长的在后面还出现过一次的子串长度
    for ln in range(len(s), 0, -1):
        for L in range(len(s) - ln + 1):
            if s[L:L + ln] in s[L + 1:]:
                print(ln)
                return
    print(0)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)