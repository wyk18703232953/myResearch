def main(n):
    # 映射 n 为字符串长度和 k（保证为偶数且不超过长度）
    length = max(2, n)
    if length % 2 == 1:
        length += 1
    k = min(length, (n // 2) * 2)
    if k <= 0:
        k = 2

    # 构造一个确定性的括号串，长度为 length
    # 前 half 个为 '('，后 half 个为 ')'，保证有解
    half = length // 2
    arr = ['('] * half + [')'] * (length - half)

    st = []
    ans = []
    for i in range(length):
        if k <= 0:
            break

        else:
            if arr[i] == '(':
                st.append((arr[i], i))

            else:
                if st and st[-1][0] == '(':
                    k -= 2
                    ans.append(st.pop())
                    ans.append((arr[i], i))

                else:
                    st.append((arr[i], i))

    ans.sort(key=lambda x: x[1])
    res = []
    for i in ans:
        res.append(i[0])
    # print(''.join(res))
    pass
if __name__ == "__main__":
    main(10)