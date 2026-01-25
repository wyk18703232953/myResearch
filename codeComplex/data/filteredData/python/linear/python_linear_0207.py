from __future__ import division
from collections import *

def main(n):
    # 根据 n 构造确定性的输入结构：
    # s 为一个固定的间隔阈值，a 为包含 n 个 (h, m) 对的列表
    # 为了让规模与 n 对应，将 n 作为时间对数量
    s = 5
    a = []
    for i in range(n):
        # 生成分散在一天中的时间点，确保确定性
        h = (i * 3) % 24
        m = (i * 7) % 60
        a.append([h, m])

    ans = -1

    for i in range(26):
        for j in range(60):
            tem = i * 60 + j
            ans = (i, j)
            for h, m in a:
                tem2 = h * 60 + m
                if tem <= tem2:
                    if tem2 - (tem + 1) < s:
                        ans = -1
                        break
                else:
                    if tem - (tem2 + 1) < s:
                        ans = -1
                        break

            if ans != -1:
                print('%d %d' % (ans[0], ans[1]))
                return

    # 如果没有找到满足条件的时间，也保持确定性行为
    print('-1 -1')


if __name__ == "__main__":
    main(10)