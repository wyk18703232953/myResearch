import math

def main(n):
    # 根据规模 n 生成测试数据：
    # 这里约定：N = n，K = n^2 作为一组规模随 n 增长的测试数据
    N = n
    K = n * n

    r = K // N
    if K % N != 0:
        r += 1

    # print(r)
    pass
if __name__ == "__main__":
    # 示例：可以修改这里的 n 以测试不同规模
    main(10)