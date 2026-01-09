import sys
import math
import bisect
import collections
import atexit

sys.setrecursionlimit(1000000)


def main(n):
    """
    n: 规模参数，用来生成 n 组 (l, r) 测试数据
    逻辑：对每组 (l, r) 计算与原程序一致的 z 并输出
    """

    # 生成测试数据：构造 n 组区间 (l, r)，这里简单生成连续区间
    # 第 i 组为 [i, i + i]，即长度为 i+1 的区间
    intervals = []
    for i in range(1, n + 1):
        l = i
        r = i + i  # 区间长度约为 2*i - i +1 = i+1
        intervals.append((l, r))

    # 按原逻辑处理每一组 (l, r)
    for l, r in intervals:
        length = r - l + 1
        z = length // 2
        if l % 2 == 0:
            z *= -1
        if length % 2 == 1:
            if r % 2 == 0:
                z += r

            else:
                z -= r
        # print(z)
        pass
if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)