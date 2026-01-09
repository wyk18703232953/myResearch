def main(n):
    # 生成确定性测试数据 a, b，规模为 n
    # 保证部分数据是合法的，也包含可能不合法的情况便于实验
    a = [i // 2 for i in range(n)]          # 非降序，约在 [0, i]
    b = [(n - 1 - i) // 2 for i in range(n)]  # 非升序，约在 [0, n-1-i]

    s = [0] * n
    ans = True

    for i in range(n):
        ans = ans and a[i] <= i and b[i] <= (n - i - 1)
        s[i] = n - a[i] - b[i]

    def qwe(arr, j):
        l, r = 0, 0
        for i in range(len(arr)):
            if i < j and arr[i] > arr[j]:
                l += 1
            elif i > j and arr[i] > arr[j]:
                r += 1
        return l, r

    if ans:
        for i in range(n):
            l, r = qwe(s, i)
            ans = ans and a[i] == l and b[i] == r

    if ans:
        # print('YES')
        pass
        for i in range(n):
            # print(n - a[i] - b[i], end=' ')
            pass
        # print()
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # 示例规模，可按需调整用于时间复杂度实验
    main(10)