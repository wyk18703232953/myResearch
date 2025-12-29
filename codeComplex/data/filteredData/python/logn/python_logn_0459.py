import random

def judge(a, b, A, B):
    """模拟交互：返回 sign((A^2 - B^2) 与 (a^2 - b^2)) 的比较结果
       >0 : (A^2 - B^2) > (a^2 - b^2)
       =0 : 相等
       <0 : (A^2 - B^2) < (a^2 - b^2)
    """
    diff_real = A * A - B * B
    diff_query = a * a - b * b
    if diff_real > diff_query:
        return 1
    if diff_real < diff_query:
        return -1
    return 0

def solve_with_judge(bit_len, A, B):
    """用与原程序等价的交互逻辑（改为调用 judge）求解 A,B"""
    # 初次询问
    e = judge(0, 0, A, B)
    # 固定为 bit_len 位长度
    astr = "0" * bit_len
    bstr = "0" * bit_len
    abig = e

    for i in range(bit_len):
        shift = 2 ** (bit_len - 1 - i)
        if abig == 0:
            e = judge(int(astr, 2) + shift, int(bstr, 2), A, B)
            if e == 1:
                continue
            else:
                if i < bit_len - 1:
                    astr = astr[:i] + "1" + astr[i + 1:]
                    bstr = bstr[:i] + "1" + bstr[i + 1:]
                else:
                    astr = astr[:i] + "1"
                    bstr = bstr[:i] + "1"
        else:
            e = judge(int(astr, 2) + shift, int(bstr, 2) + shift, A, B)
            if e == -abig:
                if abig == 1:
                    if i < bit_len - 1:
                        astr = astr[:i] + "1" + astr[i + 1:]
                    else:
                        astr = astr[:i] + "1"
                else:
                    if i < bit_len - 1:
                        bstr = bstr[:i] + "1" + bstr[i + 1:]
                    else:
                        bstr = bstr[:i] + "1"
                abig = judge(int(astr, 2), int(bstr, 2), A, B)
            else:
                e = judge(int(astr, 2) + shift, int(bstr, 2), A, B)
                if e == -1:
                    if i < bit_len - 1:
                        astr = astr[:i] + "1" + astr[i + 1:]
                        bstr = bstr[:i] + "1" + bstr[i + 1:]
                    else:
                        astr = astr[:i] + "1"
                        bstr = bstr[:i] + "1"

    return int(astr, 2), int(bstr, 2)

def main(n):
    """
    n 为规模参数：
    - 使用 bit_len = n（相当于原代码固定的 30 位）
    - 随机生成 0 <= A,B < 2^bit_len 作为测试数据
    - 返回 (A, B, 还原的A, 还原的B)
    """
    bit_len = n
    max_val = 1 << bit_len
    A = random.randrange(max_val)
    B = random.randrange(max_val)

    recA, recB = solve_with_judge(bit_len, A, B)

    # 为了符合“仅输出代码”的要求，这里不打印，只返回结果
    return A, B, recA, recB

# 示例：直接运行本文件时做一次测试
if __name__ == "__main__":
    # 例如用 30 位，对应原程序的规模
    A, B, recA, recB = main(30)
    print("True A,B   :", A, B)
    print("Found A,B  :", recA, recB)
    print("Correct    :", A == recA and B == recB)