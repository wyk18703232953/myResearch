def main(n):
    # 生成确定性的输入数据：长度为 n 的整数列表
    # 例如：a[i] = i % 5，保证有重复元素和可能的 0
    a = [i % 5 for i in range(n)]

    b = set(a)
    res = len(b)
    if 0 in b:
        res -= 1
    return res


if __name__ == "__main__":
    # 示例调用，用户可根据需要修改 n 的大小
    print(main(10))