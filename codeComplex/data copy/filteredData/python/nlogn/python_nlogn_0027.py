def main(n):
    # 确定性生成输入数据：长度为 n 的整数序列
    # 映射规则：第 i 个数为 i % (n // 2 + 1)，保证有重复元素
    if n <= 0:
        return
    num = n
    arr = [i % (n // 2 + 1) for i in range(num)]
    list_ = sorted(set(arr))
    if len(list_) == 1:
        # print("NO")
        pass

    else:
        # print(list_[1])
        pass
if __name__ == "__main__":
    main(10)