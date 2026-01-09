import sys
import math
import bisect
import collections


def main(n: int):
    # 生成规模为 n 的测试数据，这里原程序只需要一个整数 N
    N = n

    zz = ((1, -1), (0, 2), (1, -1))
    now = (0, 0)
    for i in range(N):
        # print(now[0], now[1])
        pass
        now = (now[0] + zz[i % 3][0], now[1] + zz[i % 3][1])


if __name__ == "__main__":
    # 示例运行：可根据需要修改 n 的值
    main(10)