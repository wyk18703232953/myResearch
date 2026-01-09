import math

def main(n):
    # 通过 n 确定性地生成原程序的 4 个输入：n_input, m, k, l
    # 为保证含义清晰，将 n 用作原程序中的 n_input，其余值由简单算术构造
    n_input = max(1, n)
    m = max(1, n_input // 3 + 1)
    k = n_input // 2
    l = n_input // 4

    total = k + l
    one_friend = total // m + int(total % m != 0)
    if one_friend * m > n_input:
        return -1

    else:
        return one_friend

if __name__ == "__main__":
    # 示例调用
    result = main(10)
    # print(result)
    pass