# -*- coding: utf-8 -*-
"""
改写说明：
- 移除 input()
- 封装为 main(n) 函数，其中 n 为测试规模
- 根据 n 生成测试数据：例如生成 1 到 n 的若干 k 值并逐个处理
- 保留原有核心逻辑：针对给定的 k，求无限串 "123456789101112..." 中第 k 位的数字
"""

def kth_digit(k: int) -> str:
    """返回无限串 '123456789101112...' 中第 k 位的数字（k 从 1 开始计数）"""
    sol = ''
    cnt = 0
    # i 为当前处理的数字位数：1 位数、2 位数、...、12 位数
    for i in range(1, 13):
        inc = 9 * (10 ** (i - 1)) * i  # i 位数总共贡献的位数
        if cnt + inc >= k:
            break
        else:
            cnt += inc

    lft = k - cnt
    dig = (lft) / i
    if dig != int(dig):
        dig = int(dig + 1)
    else:
        dig = int(dig)

    num = (10 ** (i - 1)) + dig - 1
    left = k - (cnt + dig * i)
    sol = str(num)
    return sol[left - 1]


def main(n: int):
    """
    根据规模 n 生成测试数据，并输出结果。
    测试数据示例：对 k = 1, 2, ..., n 分别计算对应的数字。
    """
    for k in range(1, n + 1):
        print(kth_digit(k))


if __name__ == "__main__":
    # 示例：当需要运行时，可以自行设置 n 的大小
    # main(20)
    pass