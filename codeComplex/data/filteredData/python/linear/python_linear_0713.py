def main(n):
    arr = [i + 1 for i in range(n)]
    ans = 10 ** 10
    for i in range(n):
        x = i if i > n - i - 1 else n - i - 1
        if x != 0:
            ans = min(ans, arr[i] // x)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)