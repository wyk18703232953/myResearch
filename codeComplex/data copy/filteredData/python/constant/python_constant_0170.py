import sys, collections, math, itertools, bisect
INF = sys.maxsize
mod = 1000000007

def main(n):
    if n <= 0:
        return

    # 将 n 映射为区间长度
    length = max(1, n)
    l = 1
    r = l + length - 1

    if r - l < 2:
        # print(-1)
        pass
    elif l % 2 == 0:
        # print(l, l + 1, l + 2)
        pass
    elif r - l > 2:
        # print(l + 1, l + 2, l + 3)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)