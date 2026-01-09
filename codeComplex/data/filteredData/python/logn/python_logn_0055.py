import math

def Maxxor(l, r):
    if l == r:
        return 0

    else:
        reflog = math.floor(math.log2(r))
        ref = 2 ** reflog
        if l < ref:
            return (2 * ref) - 1

        else:
            return Maxxor(l - ref, r - ref)

def main(n):
    # 规模映射：令区间 [l, r] 的长度与 n 相关
    # 确保 l < r 且数值规模随 n 增长
    if n < 2:
        n = 2
    l = n
    r = 2 * n
    ans = Maxxor(l, r)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)