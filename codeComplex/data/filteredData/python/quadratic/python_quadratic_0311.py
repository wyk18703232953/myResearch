from collections import Counter
import string
import math
from fractions import Fraction

def makedict(var):
    return dict(Counter(var))

def main(n):
    # 确定性生成 n 和 k
    # 令输入规模 n 既表示数组长度，也用于生成 k
    # 保证 k 在 [1, n] 范围内
    if n <= 0:
        return
    N = n
    K = max(1, n // 3)  # 例如 k 为 n//3，至少为 1

    # 生成长度为 N 的数组 num，元素为确定性的整数
    # 例如：num[i] = (i * 7) % 100 - 50，含有正负数
    num = [(i * 7) % 100 - 50 for i in range(N)]

    n_val = N
    k_val = K

    maxi = 0.0
    for i in range(n_val):
        count = 1
        sumt = num[i]
        for j in range(i + 1, n_val):
            sumt += num[j]
            count += 1
            if count >= k_val:
                maxi = max(maxi, sumt / count)

    if k_val == 1:
        result = max(maxi, max(num)) if num else 0.0

    else:
        result = maxi

    # 输出结果以保持与原程序一致的行为
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值做规模实验
    main(10)