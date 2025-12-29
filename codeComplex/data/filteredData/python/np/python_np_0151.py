import math, sys, bisect, heapq
from collections import defaultdict, Counter, deque
from itertools import groupby, accumulate
from functools import lru_cache
import random

int1 = lambda x: int(x) - 1
def list2d(a, b, c): return [[c] * b for _ in range(a)]
def list3d(a, b, c, d): return [[[d] * c for _ in range(b)] for _ in range(a)]
def Y(c):  print(["NO", "YES"][c])
def y(c):  print(["no", "yes"][c])
def Yy(c): print(["No", "Yes"][c])

def main(n: int):
    """
    按规模 n 生成测试数据并执行原逻辑。
    这里约定：
      - n 为数组 A 的长度
      - A[i] 在 [1, 100] 内随机生成
      - l, r, x 根据 A 的值自动生成，确保有一定概率存在合法解
    """

    # 生成测试数据
    random.seed(0)
    A = [random.randint(1, 100) for _ in range(n)]
    A.sort()

    # 根据 A 生成 l, r, x
    # 总和范围设为 [min(A), sum(A)] 里的一段
    total_sum = sum(A)
    min_val = A[0]
    max_val = A[-1]
    # 保证 l <= r 且范围不太窄
    l = random.randint(min_val, max(1, total_sum // 4))
    r = random.randint(max(l, total_sum // 4), total_sum)
    # x 为难度差下限
    x = random.randint(1, max_val - min_val if max_val > min_val else 1)

    # 为了和原代码兼容，将这些变量放在外层作用域里
    # 并在 fun 中闭包引用
    @lru_cache(None)
    def fun(pos=0, sm=-1, la=-1, tot=0):
        # pos: 当前考虑到的位置
        # sm: 当前选中题目的最小值
        # la: 当前选中题目的最大值
        # tot: 当前选中题目的总难度
        if pos == n:
            if tot >= l and tot <= r and la > 0 and (la - sm) >= x:
                return 1
            return 0
        if sm == -1:
            # 目前还没有选任何题
            return fun(pos + 1, A[pos], -1, A[pos]) + fun(pos + 1, sm, la, tot)
        elif la == -1:
            # 已有最小值 sm，但尚未确定最大值 la
            return fun(pos + 1, sm, A[pos], tot + A[pos]) + fun(pos + 1, sm, la, tot)
        else:
            # 已有最小值 sm 与最大值 la
            return fun(pos + 1, sm, A[pos], tot + A[pos]) + fun(pos + 1, sm, la, tot)

    # 输出与原程序一致：只打印 fun() 的结果
    print(fun())

if __name__ == "__main__":
    # 示例：n 可按需要修改或由外部调用 main(n)
    main(5)