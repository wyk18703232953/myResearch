from math import ceil

def main(n):
    a = [i * 2 + 1 for i in range(n)]
    ans = 10**6
    value = 10**9 + 7
    for i in range(n):
        t = ceil((a[i] - i) / n)
        tmp = i + n * t
        if tmp < value:
            value = tmp
            ans = i + 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)