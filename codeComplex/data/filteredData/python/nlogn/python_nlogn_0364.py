def main(n):
    # 映射：n -> 数组长度为 n，k 为一个与 n 相关的确定性值
    k = n // 3 + 1  # 保证 k 随规模增长，且确定性
    # 确定性构造数组：包含有一定间隔和重复模式的整数
    arr = [(i * 2 + (i // 3)) % (3 * n + 7) for i in range(n)]
    arr.sort()

    st = []
    for i in arr:
        if not st:
            st.append(i)

        else:
            while st:
                if 0 < abs(st[-1] - i) <= k:
                    st.pop()

                else:
                    break
            st.append(i)
    # print(len(st))
    pass
if __name__ == "__main__":
    main(10)