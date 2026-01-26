import math

def main(n):
    # 解释输入映射：
    # 原程序读取: N, r
    # 在这里：
    #   N = max(3, n)      # 多边形边数，至少为 3
    #   r = n              # 内接圆半径，随规模线性增长
    N = max(3, n)
    r = n

    result = r * math.sin(math.pi / N) / (1 - math.sin(math.pi / N))
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)