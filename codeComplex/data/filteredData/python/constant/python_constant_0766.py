import math

def main(n):
    # 根据规模 n 生成测试数据，这里构造 k 与 n 同量级
    # 可根据需要调整生成方式
    k = n * n  

    ans = round((-3 + math.sqrt(9 + 8 * (k + n))) / 2)
    result = n - ans
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可根据需要修改
    main(10)