def main(n):
    # 根据规模 n 生成测试数据：长度为 n 的随机由'+'和'-'组成的字符串
    # 这里简单生成一个固定模式，便于复现和测试
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    stones = 0
    for c in s:
        if c == '+':
            stones += 1
        else:
            stones -= 1
            if stones < 0:
                stones = 0

    print(stones)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)