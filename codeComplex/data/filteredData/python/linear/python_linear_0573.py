def main(n):
    if n <= 0:
        return
    if n == 1:
        print("1")
    elif n == 2:
        print("1 2")
    else:
        base = 1
        gap = 2
        cur = base
        next_val = 1
        ans = ''
        for _ in range(n - 1):
            ans += str(base) + ' '
            next_val = cur
            cur += gap
            if cur > n:
                base *= 2
                gap *= 2
                cur = base
            next_val = max(next_val, cur)
        ans += str(next_val)
        print(ans)


if __name__ == "__main__":
    main(10)