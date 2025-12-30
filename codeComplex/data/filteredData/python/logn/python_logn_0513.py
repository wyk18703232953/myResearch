def get_kth_digit(i):
    if i < 10:
        return i

    batch = 9
    count = 9
    width = 1

    while i > 10 * batch * (width + 1) + count:
        batch *= 10
        width += 1
        count += batch * width

    k = i - count - 1
    num = 10 ** width + k // (width + 1)
    return str(num)[k % (width + 1)]


def main(n):
    # 根据 n 生成测试数据：这里直接使用 n 作为查询位置
    i = n
    print(get_kth_digit(i))


if __name__ == '__main__':
    # 示例：规模 n=100，可按需修改
    main(100)