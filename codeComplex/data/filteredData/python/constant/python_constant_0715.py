from math import *
from fractions import *

def main(n):
    # 确定性生成 k，保证 1 <= k <= n
    # 这里选择一个与 n 相关但不等于 1 的 k（除非 n == 1）
    if n <= 0:
        return
    if n == 1:
        k = 1

    else:
        k = n // 2
        if k < 1:
            k = 1

    if k == 1:
        ans = "1" + "0" * (n - 1)

    else:
        a = (n - k) // 2
        p = "1" + "0" * a
        ans = p * (n // (a + 1)) + p[:(n % (a + 1))]
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小进行时间复杂度实验
    main(10)