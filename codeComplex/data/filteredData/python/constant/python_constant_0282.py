from math import *
from cmath import *
from itertools import *
from decimal import *
from fractions import *
from sys import *
from types import CodeType, new_class

def main(n: int):
    """
    根据规模 n 生成测试数据（这里只是演示，原逻辑仅用到 n 本身）。
    输出与原程序等价的结果：n // 2 + 1
    """
    # 如果需要生成更复杂的测试数据，可在此基于 n 构造。
    # 当前原始代码只依赖单个整数 n，因此直接使用传入的 n。
    result = n // 2 + 1
    print(result)


if __name__ == "__main__":
    # 示例：自行指定 n 运行测试
    # 可修改这里的值进行简单测试
    main(10)