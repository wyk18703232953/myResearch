from collections import defaultdict as dc
from collections import Counter
from bisect import bisect_right, bisect_left
import math
from operator import itemgetter
from heapq import heapify, heappop, heappush
from queue import PriorityQueue as pq

def main(n: int):
    # 这里根据 n 生成测试数据，如果需要可以扩展为更复杂的生成逻辑
    # 当前原始代码只用到 n，本行只是体现“生成测试数据”的位置
    test_n = n

    if test_n <= 5:
        print(-1)
    else:
        for i in range(2, 5):
            print(1, i)
        for i in range(5, test_n + 1):
            print(2, i)
    for i in range(2, test_n + 1):
        print(1, i)


if __name__ == "__main__":
    # 示例：调用 main(10)，可按需修改或在其他模块中调用 main(n)
    main(10)