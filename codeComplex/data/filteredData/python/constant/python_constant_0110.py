def main(n):
    cases = n
    total_ans = 0
    for i in range(1, cases + 1):
        a = i
        b = 2 * i
        ans = 0
        x, y = a, b
        while x > 0 and y > 0:
            if x < y:
                x, y = y, x
            ans += x // y
            x = x % y
        total_ans += ans
    # print(total_ans)
    pass
if __name__ == "__main__":
    main(10)