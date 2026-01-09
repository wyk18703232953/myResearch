def check(st, n):
    count = 1
    i = 1
    pre = st[0]
    pre_indx = 0
    indx = [0 for _ in range(n)]
    while i < n:
        if pre != st[i]:
            count += 1

        else:
            indx[pre_indx] = count
            count = 1
            pre_indx = i
        pre = st[i]
        i += 1
    indx[pre_indx] = count
    return indx

def main(n):
    if n <= 0:
        return
    # 生成确定性的字符串，周期为 3
    # 例如 n=1: "a", n=5: "abaca", n=7: "abacaba"
    chars = ['a', 'b', 'a', 'c', 'a', 'b', 'a']
    st = ''.join(chars[i % len(chars)] for i in range(n))

    actual_indx = check(st, n)
    reverse_indx = check(st[::-1], n)

    if st[0] == st[-1]:
        result = max(actual_indx)

    else:
        result = min(n, max(max(actual_indx[1:]), actual_indx[0] + reverse_indx[0]))
    # print(result)
    pass
if __name__ == "__main__":
    main(10)