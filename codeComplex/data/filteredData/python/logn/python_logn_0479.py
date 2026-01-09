from math import inf

mod = 1000000007
INF = inf

def main(n):
    """
    n: 规模参数，用来生成测试数据。
       这里我们把需要查询的第 k 位数字设置为 k = n。
       （原始程序是：输入一个整数 k，输出无限正整数序列
        123456789101112... 中的第 k 位数字）
    返回：对应的数字字符（类型为 str）
    """

    # 原逻辑：读取输入的 k，然后用 k-1 作为 0-based 下标
    k = n
    k -= 1

    pre = 0      # 已经跨过的位数总和
    cur = 1      # 当前处理的数字的位数（1 位数、2 位数、...）
    point = 1    # 当前有多少位的数（1 位数时 cur=1, point=1）

    # 找到第 k 位所在的“位数区间”
    # 1 位数贡献：9 * 1 * 1
    # 2 位数贡献：90 * 2 = 9 * 10 * 2
    # 3 位数贡献：900 * 3 = 9 * 100 * 3
    while pre + 9 * cur * point < k:
        pre += 9 * cur * point
        cur *= 10
        point += 1

    # 在该区间内的偏移
    k -= pre
    num, pos = divmod(k, point)
    # 区间起点数：10^(point-1)
    num += pow(10, point - 1)

    # 返回对应位置的数字字符
    return str(num)[pos]


if __name__ == "__main__":
    # 示例：调用 main(n) 并打印结果
    # 这里使用 n = 15 作为测试规模，你可以自行修改
    test_n = 15
    # print(main(test_n))
    pass