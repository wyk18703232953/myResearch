def main(n):
    # 映射：n -> 数组长度 = n, k = n // 2
    k = n // 2 if n > 0 else 0
    # 生成确定性数组：包含正负、重复及间距多样的整数
    arr = [((i * 7) % (2 * n + 1)) - n for i in range(n)] if n > 0 else []
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