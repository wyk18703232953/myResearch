def main(n):
    # 解释规模含义：
    # n -> 列表长度，m 固定为 n
    m = n
    # 构造一个确定性的数组 a，元素大小与 n 相关
    # 示例构造：a[i] = (i * 2) % (n + 3) + 1，保证正整数且有重复
    a = [((i * 2) % (n + 3)) + 1 for i in range(m)]

    a.sort()
    res = 0
    same = 0
    p = 1
    for h in a:
        if p <= h:
            p += 1
        else:
            same += 1
    res = a[-1] + same
    result = sum(a) - res
    print(result)
    return result


if __name__ == "__main__":
    # 示例：使用 n = 10 进行一次规模为 10 的实验
    main(10)