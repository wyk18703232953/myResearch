def main(n):
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(max(n, 1)))

    def check_x(mid):
        ans = 'no'
        d = {}
        for i in range(len(s) - mid + 1):
            if s[i:i + mid] in d:
                ans = 'yes'
                break
            d[s[i:i + mid]] = 1
        return ans

    l = 0
    r = len(s) - 1
    while r - l > 1:
        mid = (r + l) // 2
        ans = check_x(mid)
        if ans == 'yes':
            l = mid

        else:
            r = mid

    if check_x(r) == 'yes':
        # print(r)
        pass

    else:
        # print(l)
        pass
if __name__ == "__main__":
    main(10)