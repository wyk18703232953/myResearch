def main(n):
    # 生成确定性输入列表：长度为 n，元素为 i % (n // 2 + 1)
    # 这样可以保证有重复元素，便于体现集合去重逻辑
    l = [i % (n // 2 + 1) for i in range(n)]
    s = set(l)
    x = 0
    if x in s:
        # print(len(s) - 1)
        pass

    else:
        # print(len(s))
        pass
if __name__ == "__main__":
    main(10)