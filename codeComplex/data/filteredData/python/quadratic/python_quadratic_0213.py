# qumeric (refactored without input, with main(n))

from operator import *

def main(n):
    """
    根据规模 n 生成测试数据并执行原逻辑。
    这里的“生成测试数据”策略：
    - 设比特长度 m = max(1, n.bit_length())，保证随 n 增长而增加状态空间。
    - 构造 n 个长度为 m 的二进制字符串，保证有一定多样性。
    """

    # 比特长度随 n 增长
    m = max(1, n.bit_length())

    # 简单的可重复测试数据生成方案：
    # 第 i 行对应一个整数 val，再转为长度为 m 的二进制串。
    a = []
    for i in range(n):
        # 通过线性同余 + i 的方式生成分布较均匀的数字
        val = (i * 1103515245 + 12345) & ((1 << m) - 1)
        a.append(val)

    s = 0
    t = 0
    for x in a:
        t |= s & x
        s |= x

    # 原代码逻辑：如果存在 x 使得 x & s & ~t 为真，则输出 "YES"，否则 "NO"
    result = ("YES", "NO")[all(x & s & ~t for x in a)]
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)