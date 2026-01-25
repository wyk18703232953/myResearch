def main(n):
    # 生成确定性的测试数据
    # l1: 长度为 n，每个元素为 "a{i}"
    # l2: 长度为 n，每个元素为 "a{i//2}"，保证有重复和缺失情况
    l1 = ["a{}".format(i) for i in range(n)]
    l2 = ["a{}".format(i // 2) for i in range(n)]

    c = 0
    # 保持原逻辑：对于 l1 中每个元素，如果在 l2 中出现则删掉一次，否则计数加一
    for i in range(n):
        if l1[i] in l2:
            l2.remove(l1[i])
        else:
            c += 1

    print(c)


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)