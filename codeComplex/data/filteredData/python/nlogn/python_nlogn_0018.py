def main(n):
    # 生成确定性输入列表：长度为 n，包含一些重复元素
    # 示例构造：x[i] = (i * 2) % (n // 2 + 1) 保证有重复
    if n <= 0:
        return
    x = [(i * 2) % (n // 2 + 1) for i in range(n)]
    x = list(set(x))
    x.sort()
    if len(x) != 1:
        print(x[1])
    else:
        print("NO")


if __name__ == "__main__":
    main(10)