def ballbuster5000(arr, rj):
    for i in arr:
        rj += i
    gg = 0
    i = 0
    while gg <= rj:
        gg += arr[i]
        rj -= arr[i]
        i -= -1
    return i


def main(n):
    if n <= 0:
        return
    x = [i % 7 - 3 for i in range(1, n + 1)]
    x.sort(reverse=True)
    result = ballbuster5000(x, 0)
    print(result)


if __name__ == "__main__":
    main(10)