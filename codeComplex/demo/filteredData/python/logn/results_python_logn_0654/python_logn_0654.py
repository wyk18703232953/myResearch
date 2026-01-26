import math
from collections import defaultdict

def main(n):
    # 映射：保持 k 为一个与 n 有简单确定性关系的整数
    # 原程序中没有对输入做约束关系，这里设定 k = n // 2
    k = n // 2
    ans = 0
    for i in range(1, 1000001):
        val = (i * (i + 1)) // 2
        if val - (n - i) == k:
            ans = n - i
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：以 n = 10 作为输入规模调用
    main(10)