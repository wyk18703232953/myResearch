import logging
from collections import defaultdict

logging.root.setLevel(level=logging.DEBUG)


def main(n):
    # 生成确定性的字符串，长度为 n
    # 使用简单周期模式，避免过度压缩或全异
    if n <= 0:
        # print(0)
        pass
        return

    base = "abcde"
    s = "".join(base[i % len(base)] for i in range(n))

    substr = defaultdict(int)
    for left in range(len(s)):
        for right in range(left + 1, len(s) + 1):
            substr[s[left:right]] += 1

    max_len = 0
    for segment, times in substr.items():
        if times >= 2:
            max_len = max(max_len, len(segment))
    # print(max_len)
    pass
if __name__ == "__main__":
    main(10)