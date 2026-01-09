def prefix_sums(A):
    n = len(A)
    P = [0] * n
    P[0] = A[0]
    for k in range(1, n):
        P[k] = int((P[k - 1] + A[k]) % (1e9+7))
    return P

def main(n):
    global arr, s
    arr = [[0] * n for _ in range(n)]
    s = ''.join('f' if i % 2 == 0 else 's' for i in range(n))

    def find_ans():
        idx = 0
        for i in range(len(arr)-1):
            arr[0][0] = 1

            if s[i] == 'f':
                for j in range(0, len(arr)):
                    arr[i+1][0] = 0
                    if j > 0:
                        arr[i+1][j] = arr[i][j-1]
                        idx = i+1

            else:
                val = 0
                arr[i+1] = prefix_sums(arr[i][::-1])[::-1]
        return arr

    if n == 1 or 'f' not in s:
        if s[0] == 's':
            return 1

        else:
            return int(sum(find_ans()[-1]) % (1e9+7))

    else:
        return int(sum(find_ans()[-1]) % (1e9+7))

if __name__ == "__main__":
    # print(main(10))
    pass