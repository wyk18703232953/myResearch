import math
import bisect
from collections import *


def main(n):
    # 保持与原程序一致的核心逻辑，仅将输入改为参数 n
    if n == 2 or n == 3 or n == 4 or n == 5:
        print(-1)
    else:
        print(1, 2)
        print(2, 3)
        print(2, 4)
        for i in range(5, n + 1):
            print(4, i)

    for i in range(2, n + 1):
        print(1, i)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值做规模实验
    main(10)