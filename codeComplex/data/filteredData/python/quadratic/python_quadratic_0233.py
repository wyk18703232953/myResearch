from collections import Counter
import string
import math
from fractions import Fraction

def array_int_from_list(lst):
    return [int(i) for i in lst]

def vary_from_value(value):
    return int(value)

def makedict(var):
    return dict(Counter(var))

def core_logic(n, indices, cost):
    ans = float('inf')
    mint = []
    for i in range(n):
        ans = float('inf')
        total = cost[i]
        flag = 0
        for j in range(i):
            if indices[i] > indices[j]:
                ans = min(ans, cost[j])
                flag = 1
        if flag != 0:
            total += ans
            ans = float('inf')
            flag = 0
            for k in range(i + 1, n):
                if indices[k] > indices[i]:
                    ans = min(ans, cost[k])
                    flag = 1
            if flag != 0:
                total += ans
                mint.append(total)

            else:
                continue

        else:
            continue
    if len(mint) > 0:
        return min(mint)

    else:
        return -1

def generate_data(n):
    # n 作为规模参数：数组长度
    # indices 严格递增，使得逻辑路径充分被触发
    indices = [i + 1 for i in range(n)]
    # cost 使用简单确定性模式：重复 1..5
    cost = [(i % 5) + 1 for i in range(n)]
    return n, indices, cost

def main(n):
    n_value, indices, cost = generate_data(n)
    result = core_logic(n_value, indices, cost)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)