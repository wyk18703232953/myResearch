def main(n):
    # 生成长度为 n 的整数列表，元素构造为 i % (n // 2 + 1)，保证确定性
    a = [i % (n // 2 + 1) for i in range(n)]
    s = set(a)
    s.discard(0)
    print(len(s))

if __name__ == "__main__":
    main(10)