import sys
from collections import deque
import bisect

def chk(l, r, total):
    b = len(l)
    prev = 0
    i = 0
    f = 1
    cnt = 0
    while i < b:
        prev = prev + l[i]
        if cnt == total and prev == r:
            i = i + 1
            continue

        if prev == r:
            cnt += 1
            if cnt != total:
                prev = 0

        i = i + 1

    if cnt < total or i != b:
        f = 0

    return f

def main(n):
    # 生成长度为 n 的数字串 s
    # 构造方式：s[i] = (i % 9) + 1，保证都是 '1' 到 '9'
    s = ''.join(str((i % 9) + 1) for i in range(n))

    l = []
    som = 0
    for ch in s:
        l.append(int(ch))
        som += int(ch)

    flag = 0
    for i in range(2, n + 1):
        if som % i == 0:
            r = som // i
            if chk(l, r, i):
                flag = 1
                break

        if flag:
            break

    if flag:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # 示例调用：可根据需要调整 n 的值进行规模实验
    main(10)