def main(n):
    # 确定性生成输入结构：
    # 对应原程序的含义：
    #   - 字符串长度为 n
    #   - k 为不超过 n 的最大偶数
    #   - 字符串为 n/2 个 '(' 再接 n/2 个 ')'（若 n 为奇数，最后一个为 '('）
    if n <= 0:
        return

    if n % 2 == 0:
        k = n
        s = "(" * (n // 2) + ")" * (n // 2)
    else:
        k = n - 1
        s = "(" * (n // 2) + ")" * (n // 2) + "("

    if n == k:
        print(s)
    else:
        ans = []
        arr = []
        for ch in s:
            arr.append(ch)

        for i in range(n):
            if len(ans) == k // 2:
                break
            if arr[i] == '(':
                ans.append(i)

        for i in range(n - 1, -1, -1):
            if len(ans) == k:
                break
            if arr[i] == ')':
                ans.append(i)

        ans.sort()
        for i in ans:
            print(arr[i], end="")

if __name__ == "__main__":
    main(10)