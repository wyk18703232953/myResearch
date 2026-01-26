import math

def main(n):
    # 对应原始输入结构：两个浮点数 n_float, r
    # 在这里用 n 作为 n_float 的规模参数，r 由 n 确定性生成
    if n <= 0:
        return
    n_float = float(n)
    r = float(n) + 0.5
    a = math.pi / n_float
    s = math.sin(a)
    R = (r * s) / (1 - s)
    # print(R)
    pass
if __name__ == "__main__":
    main(100000)