# https://codeforces.com/problemset/problem/909/D

import random
import string

def process(a):
    assert len(a) >= 2

    n = len(a)
    min_ = float('inf')

    for i, (cnt, c) in enumerate(a):
        if i == 0 or i == n - 1:
            min_ = min(min_, cnt)
        else:
            min_ = min(min_, (cnt + 1) // 2)

    b = []
    for i, (cnt, c) in enumerate(a):
        if i == 0 or i == n - 1:
            remain = cnt - min_
        else:
            remain = cnt - min_ * 2

        if remain <= 0:
            continue

        if len(b) == 0 or c != b[-1][1]:
            b.append([remain, c])
        else:
            pre_cnt, pre_c = b.pop()
            b.append([pre_cnt + remain, c])

    return b, min_


def main(n: int):
    # 1. 生成规模为 n 的测试数据字符串 S
    # 使用小写字母随机生成长度为 n 的字符串
    alphabet = string.ascii_lowercase
    S = ''.join(random.choice(alphabet) for _ in range(n))

    # 2. 按原逻辑处理 S
    S += ' '
    cur = []

    cnt = 0
    pre = ''
    for x in S:
        if cnt == 0:
            cnt += 1
            pre = x
        elif x != pre:
            cur.append([cnt, pre])
            cnt = 1
            pre = x
        else:
            cnt += 1

    cnt = 0
    while len(cur) not in [0, 1]:
        cur, min_ = process(cur)
        cnt += min_

    print(cnt)


if __name__ == "__main__":
    # 示例：调用 main，规模设为 10
    main(10)