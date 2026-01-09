def main(n):
    # 确定性生成长度为 n 的字符串：周期性重复 'abcde'
    base = "abcde"
    s = "".join(base[i % len(base)] for i in range(n))

    # 原算法逻辑：寻找最长重复子串长度
    for l in range(len(s), 0, -1):
        k = []
        for i in range(0, len(s) - l + 1):
            k.append(s[i:i + l])
        if len(k) != len(list(set(k))):
            # print(l)
            pass
            return
    # print(0)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的大小做时间复杂度实验
    main(1000)