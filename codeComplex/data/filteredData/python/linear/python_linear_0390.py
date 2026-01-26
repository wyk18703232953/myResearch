import sys
from bisect import *

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
M = 998244353
EPS = 1e-6

def Ceil(a, b):
    return a // b + int(a % b > 0)

def main(n):
    # 确定性生成输入数据
    # n 对应原程序中的 n，数组 a 的长度为 n
    # a[i] = (i * 3 + 7) % M
    a = [(i * 3 + 7) % M for i in range(n)]

    series = [1]
    fact = 1
    for i in range(n + 1):
        series.append(((series[-1] * 2) % M + fact) % M)
        fact = (fact * 2) % M

    ind = n - 1
    ans = 0
    for i in range(n):
        ans = (ans + (a[i] * series[ind]) % M) % M
        ind -= 1

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 的规模做复杂度实验
    main(10)