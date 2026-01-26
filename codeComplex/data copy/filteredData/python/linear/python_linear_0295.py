def main(n):
    # n 表示列表长度
    l = [i % (n // 2 + 1) for i in range(n)]
    s = set(l)
    if 0 in s:
        # print(len(s) - 1)
        pass

    else:
        # print(len(s))
        pass
if __name__ == "__main__":
    main(10)