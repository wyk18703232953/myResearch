def prefix_sums(A):
    n = len(A)
    P = [0] * n
    P[0] = A[0]
    for k in range(1, n):
        P[k] = int((P[k - 1] + A[k]) % (1e9 + 7))
    return P


def find_ans(arr, s):
    idx = 0
    for i in range(len(arr) - 1):
        arr[0][0] = 1
        if s[i] == 'f':
            for j in range(0, len(arr)):
                arr[i + 1][0] = 0
                if j > 0:
                    arr[i + 1][j] = arr[i][j - 1]
                    idx = i + 1
        else:
            arr[i + 1] = prefix_sums(arr[i][::-1])[::-1]
    return arr


def main(n):
    if n <= 0:
        return 0

    arr = [[0] * n for _ in range(n)]

    # 确定性生成长度为 n 的指令串 s，元素为 'f' 或 's'
    # 例如：偶数位置用 'f'，奇数位置用 's'
    s = ''.join('f' if i % 2 == 0 else 's' for i in range(n))

    if n == 1 or 'f' not in s:
        if s[0] == 's':
            ans = 1
        else:
            ans = int(sum(find_ans(arr, s)[-1]) % (1e9 + 7))
    else:
        ans = int(sum(find_ans(arr, s)[-1]) % (1e9 + 7))
    print(ans)
    return ans


if __name__ == "__main__":
    main(5)