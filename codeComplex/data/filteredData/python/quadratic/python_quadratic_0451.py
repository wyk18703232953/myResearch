def main(n):
    # 生成确定性输入：长度为 n 的排列 L（1..n 的简单循环移位）
    if n <= 0:
        return
    L = [(i % n) + 1 for i in range(n)]

    ans = [''] * n
    revL = [0] * n
    ans[-1] = 'B'
    for i in range(n):
        revL[L[i] - 1] = i + 1
    for i in range(n - 2, -1, -1):
        t = revL[i] - 1
        counter = 'B'
        for j in range(t, -1, -i - 1):
            if j == t:
                continue
            if ans[L[j] - 1] == 'B':
                counter = 'A'
                break
        if counter != 'A':
            for k in range(t, n, i + 1):
                if k == t:
                    continue
                if ans[L[k] - 1] == 'B':
                    counter = 'A'
                    break
        ans[i] = counter
    for i in range(n):
        # print(ans[L[i] - 1], sep='', end='')
        pass
if __name__ == "__main__":
    main(10)