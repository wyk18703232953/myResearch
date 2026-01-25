def main(n):
    # n 作为列表长度规模
    if n <= 1:
        xs = [0] * n
    else:
        # 构造一个有重复元素的确定性序列
        # 规律：xs[i] = i % (n // 2 + 1)
        base = n // 2 + 1
        xs = [i % base for i in range(n)]

    res = 0
    xs = xs[:]  # 复制一份以防修改外部引用

    while xs:
        if len(xs) == 1:
            break
        j = xs.index(xs[0], 1)
        res += j - 1
        xs = xs[1:j] + xs[j+1:]

    print(res)
    return res


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的值
    main(10)