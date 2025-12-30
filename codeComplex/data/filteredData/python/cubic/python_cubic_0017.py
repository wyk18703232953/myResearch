import logging
import random
import string
from collections import defaultdict

logging.root.setLevel(level=logging.DEBUG)


def main(n: int):
    # 1. 根据规模 n 生成测试数据：长度为 n 的随机小写字母串
    s = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    # 2. 原始逻辑：统计所有子串出现次数，并求出现至少两次的最长子串长度
    substr = defaultdict(int)
    for left in range(len(s)):
        for right in range(left + 1, len(s) + 1):
            substr[s[left:right]] += 1

    max_len = 0
    for segment, times in substr.items():
        if times >= 2:
            max_len = max(max_len, len(segment))

    print(max_len)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改 n
    main(10)