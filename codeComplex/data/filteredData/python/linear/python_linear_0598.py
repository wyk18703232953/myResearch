from __future__ import division

def main(n):
    out = 0
    for i in range(2, n + 1):
        out += 4 * (n // i - 1) * i
    print(out)


if __name__ == "__main__":
    # 示例：根据规模 n 生成测试数据，这里直接使用 n 作为参数。
    # 可按需修改 n 的取值来做测试。
    test_n = 10
    main(test_n)