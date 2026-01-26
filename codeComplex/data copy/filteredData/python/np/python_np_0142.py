def main(n):
    # 为保持原算法的输入结构 (n, m)，这里将 m 设为与 n 相关的确定性值
    # 选择 m = n * (n + 1)，既随规模变化，又保证完全确定
    m = n * (n + 1)

    out = [n]
    i = n - 1
    m -= 1
    for _ in range(n - 1):
        if m % 2:
            out.append(i)
        else:
            out = [i] + out
        m //= 2
        i -= 1

    for x in out:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    # 示例调用：可按需修改 n 以进行规模实验
    main(10)