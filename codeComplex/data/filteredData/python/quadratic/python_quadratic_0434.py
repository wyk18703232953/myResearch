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

def generate_input(n):
    if n <= 0:
        n = 1
    # n 作为字符串长度；构造一个确定性的 0/1 串
    # 数位模式：第 i 位为 (i * 7 + 3) % 10，再对 2 取模
    digits = [(i * 7 + 3) % 2 for i in range(n)]
    s = "".join(str(d) for d in digits)
    return n, s

def core_logic(n, s):
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
    return "YES" if flag else "NO"

def main(n):
    n_in, s = generate_input(n)
    result = core_logic(n_in, s)
    print(result)

if __name__ == "__main__":
    main(10)