import math

def main(n):
    # 生成确定性的 r，映射规模：n 为原程序中的 n，r = n 的简单线性关系
    r = n

    x = math.sin(math.pi / n)
    y = (x * r) / (1 - x)

    # print(y)
    pass
if __name__ == "__main__":
    main(10)