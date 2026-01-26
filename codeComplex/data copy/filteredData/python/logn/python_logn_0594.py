import math


def main(n: int):
    # 生成确定性的 k，与 n 同阶，便于规模实验
    k = n // 2
    result = round(n + 1.5 - math.sqrt(2 * (n + k) + 2.75))
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 10 进行调用
    main(10)