# -*- coding:utf-8 -*-

def main(n):
    """
    n 为规模参数：
    - 这里将 n 作为要查询的第 n 个数字（与原程序中的 k 等价）
    - 自动生成测试数据：k = n
    - 返回该位置上的数字字符
    """
    k = n
    k -= 1  # 字符串起始从0
    num_len, count_per_len = 1, 9  # num_len: 当前数字长度; count_per_len: 该长度下的数字个数

    # 找到第 k 位落在哪个长度区间
    while k > num_len * count_per_len:
        k -= num_len * count_per_len
        num_len += 1
        count_per_len *= 10

    # 所属的具体数字
    start = 10 ** (num_len - 1)
    target_num = start + k // num_len
    digit_index = k % num_len
    x = str(target_num)[digit_index]

    print(x)
    return x


if __name__ == "__main__":
    # 示例：查询第 15 个数字
    main(15)