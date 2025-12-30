import math
from collections import defaultdict, deque
import random
import string

def main(n):
    # 生成测试数据：
    # n: 字符串长度
    # k: 拼接次数，设为 n（可按需调整策略）
    k = n

    # 生成长度为 n 的随机小写字母串
    st = ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

    res = st
    pos = 1
    cnt = 1

    # 原逻辑：构造尽量短的最终串，使其包含 k 段，且每次拼接尽量利用前后缀重叠
    while cnt < k:
        suffix = 0
        counter = 0
        # 检查当前位置 pos 开始，res 的后缀与 st 的前缀最长匹配长度
        for i in range(pos, len(res)):
            if res[i] == st[suffix]:
                suffix += 1
            else:
                counter = 1
                break
        if counter:
            pos += 1
            continue
        if pos > len(res):
            res += st
            cnt += 1
            pos += 1
            continue
        res += st[suffix:n]
        cnt += 1
        pos += 1

    print(res)