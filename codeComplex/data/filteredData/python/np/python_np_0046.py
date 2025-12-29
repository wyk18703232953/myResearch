import math
import random

def main(n):
    # 生成测试数据：
    # 目标串 x：长度 n，由 '+' 和 '-' 组成
    # 观测串 y：长度 n，由 '+', '-', '?' 组成
    x = ''.join(random.choice(['+', '-']) for _ in range(n))
    y = ''.join(random.choice(['+', '-', '?']) for _ in range(n))

    goal = x.count('+') - y.count('+')
    options = y.count('?')

    if options == 0:
        if goal == 0:
            print(1)
        else:
            print(0)
    else:
        if goal > options or goal < 0:
            print(0)
        else:
            result = (math.factorial(options) /
                      (math.factorial(goal) *
                       math.factorial(options - goal) *
                       (2 ** options)))
            print(result)

# 示例调用：可以在其他地方调用 main(n)
# main(10)