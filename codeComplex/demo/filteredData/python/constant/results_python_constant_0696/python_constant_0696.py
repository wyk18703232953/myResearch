import math

def main(n):
    # 映射：原程序中有两个输入 n, r
    # 这里将第一个输入固定为 n，第二个输入 r 由 n 确定性生成
    # 例如 r = n 的平方，保证随规模变化
    input_n = n
    r = n * n

    # 原始核心逻辑
    result = r / (1 / math.cos(math.pi * (input_n - 2) / 2 / input_n) - 1)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)