from bisect import bisect_right
from random import randint
from sys import setrecursionlimit

setrecursionlimit(15000)


def get_gdict(arr):
    gdict = dict()
    for x in arr:
        gdict[x] = gdict.get(x, 0) + 1
    return gdict


def initial_check(barr, garr):
    for x in garr:
        if x < barr[-1]:
            return False
    return True


def main(n):
    """
    n 作为规模参数：
    - 生成 n 个 barr 元素
    - 生成 m 个 garr 元素，其中 m 在 [1, n] 范围内
    元素值随机在 [1, 10^9] 范围内生成，并保证 initial_check 尽可能有机会为 True。
    返回计算得到的 ans（或者 -1）。
    """
    # 生成测试数据
    # 规模参数 n：barr 长度为 n，garr 长度 m ∈ [1, n]
    m = max(1, n)  # 简单设定：m = n，也可以改成任意 1..n
    # 生成 barr
    barr = [randint(1, 10**9) for _ in range(n)]
    barr.sort()
    # 为了提高 initial_check 为 True 的概率，让 garr 的元素不小于 barr[-1] 的概率较大
    base = barr[-1] if barr else 1
    garr = [base + randint(0, 10**6) for _ in range(m)]
    garr.sort()

    # 以下为原逻辑的移植，仅去掉输入与打印，改为返回 ans
    ans = 0
    gdict = get_gdict(garr)

    if initial_check(barr, garr):
        count = m
        b = n - 1
        g = m - 1
        while count > 0 and b >= 0:
            tempb = [barr[b]] * m
            for i in range(len(tempb)):
                if count <= 0:
                    # 注意：原代码此处有 ans += tempb[b] 的 bug（b 用错）
                    # 为保持语义不变，仍然保留错误写法
                    for j in range(i, m):
                        ans += tempb[b]
                    break

                if tempb[i] in gdict:
                    gdict[tempb[i]] -= 1
                    ans += tempb[i]
                    count -= 1
                    if gdict[tempb[i]] == 0:
                        del gdict[tempb[i]]
                else:
                    if i == 0:
                        ans += tempb[i]
                        continue
                    for k in range(g, -1, -1):
                        if garr[k] in gdict:
                            ans += garr[g]
                            g = k - 1
                            count -= 1
                            break
            b -= 1

        while b >= 0:
            ans += m * barr[b]
            b -= 1
        return ans
    else:
        return -1


# 简单示例调用（提交到评测系统时可删除或保留）
if __name__ == "__main__":
    # 示例：规模 n = 5
    print(main(5))