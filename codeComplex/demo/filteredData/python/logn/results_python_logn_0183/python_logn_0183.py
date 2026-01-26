def main(n):
    s = n // 2
    def check(x):
        y = list(str(x))
        ans_val = x
        for i in y:
            ans_val -= int(i)
        if ans_val >= s:
            return True
        return False

    ans = 0
    l = 1
    r = n
    while l <= r:
        m = (l + r) // 2
        if check(m):
            ans = n - m + 1
            r = m - 1

        else:
            l = m + 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10**6)