def main(n):
    # 生成长度为 n 的确定性整数列表
    # 第 i 个元素为 (i * 7) % (n + 5)，确保有一定波动但完全确定
    li = [(i * 7) % (n + 5) for i in range(n)] if n > 0 else []

    if not li:
        print("NO")
        return

    x = li.index(max(li))
    if li[:x] == sorted(li[:x]) and li[x:] == sorted(li[x:])[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(10)