# coding: utf-8
import sys
sys.setrecursionlimit(int(1e7))

def main(n):
    # 这里的 n 视为规模参数，可根据需要生成测试数据
    # 原逻辑只依赖于一个整数 n，故直接使用该 n
    result = 2 * (n * (n - 1)) + 1
    print(result)
    return

if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据，这里直接使用一个示例规模
    # 可在此处修改为任何需要测试的 n
    test_n = 10
    main(test_n)