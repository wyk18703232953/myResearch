# -*- coding: utf-8 -*-

import random
import string

def main(n: int):
    # 1. 生成测试数据：长度为 n 的随机小写字母串
    #    可根据需要修改为其他字符集或结构化数据
    if n <= 0:
        return 0

    letters = string.ascii_lowercase
    s = ''.join(random.choice(letters) for _ in range(n))

    # 2. 原逻辑：求字符串中最长重复子串的长度（暴力枚举）
    m = 0
    for i in range(n - 1):
        for j in range(i, n + 1):
            # s[i:j] 在 s[i+1:n] 中出现，且长度大于当前 m
            if len(s[i:j]) > m and s[i:j] in s[i + 1:n]:
                m = len(s[i:j])

    print(m)
    return m

if __name__ == "__main__":
    # 这里给一个默认规模，可根据需要修改或在外部调用 main(n)
    main(10)