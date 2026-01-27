from math import ceil

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里示例选择 k 为 n 的一半向上取整，且至少为 1
    k = max(1, (n + 1) // 2)

    r = 2 * n
    g = 5 * n
    b = 8 * n

    result = ceil(r / k) + ceil(g / k) + ceil(b / k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)