from math import ceil

def main(n):
    # 示例：根据规模 n 生成 k
    # 这里设定 k = max(1, n // 3) 作为一组可行的测试数据
    k = max(1, n // 3)

    result = ceil(n * 2 / k) + ceil(n * 5 / k) + ceil(n * 8 / k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的值进行测试
    main(10)