def main(n: int):
    # 根据规模 n 生成测试数据，这里用一个长度为 n 的只含 '1' 和 '2' 的串
    # 示例策略：前 n//2 个为 '1'，后面的为 '2'
    s = '1' * (n // 2) + '2' * (n - n // 2)

    t = s.count('1')
    s_no1 = s.replace('1', '')
    i = s_no1.find('2')
    if i == -1:
        result = s_no1 + '1' * t
    else:
        result = s_no1[:i] + '1' * t + s_no1[i:]
    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)