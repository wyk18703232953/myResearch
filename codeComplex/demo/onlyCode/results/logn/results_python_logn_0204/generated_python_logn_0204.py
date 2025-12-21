def main(n):
    s = n // 2
    if s >= n:
        return 0
    i = s
    while i <= n + 1:
        l = 0
        for j in str(i):
            l += int(j)
        if i - l >= s:
            break
        i += 1
    return max(0, n - i + 1)

if __name__ == "__main__":
    print(main(100000))