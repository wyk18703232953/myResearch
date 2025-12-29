def main(n):
    # 根据规模 n 生成测试数据，这里示例为：
    # l = 0, r = n，用于放大区间范围
    l = 0
    r = n

    diff = (r ^ l)
    ans = (1 << diff.bit_length()) - 1
    print(ans)


if __name__ == "__main__":
    # 示例：将规模设为 10
    main(10)