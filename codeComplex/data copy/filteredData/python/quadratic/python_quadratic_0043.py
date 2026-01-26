modulo = int(1e9 + 7)

def main(n):
    if n <= 0:
        # print(1)
        pass
        return

    # deterministic generation of arr with 'f' and 's' pattern
    # pattern: arr[i] = 'f' if i % 3 == 0 else 's'
    arr = ['f' if i % 3 == 0 else 's' for i in range(n)]

    dp = [1]
    for i in range(n):
        if arr[i] == 'f':
            dp.append(0)
            continue
        for j in range(1, len(dp)):
            dp[j] = (dp[j] + dp[j - 1]) % modulo
    # print(dp[-1])
    pass
if __name__ == "__main__":
    main(10)