def main(n):
    # 确定性生成长度为 n 的整数序列
    a = [(i * 2 + (i % 3)) for i in range(n)]

    st = [a[0]] if n > 0 else []
    for i in range(1, n):
        if st and st[-1] % 2 == a[i] % 2:
            st.pop()
        else:
            st.append(a[i])
    if len(st) <= 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：输入规模为 10
    main(10)