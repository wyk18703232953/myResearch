def main(n):
    s = ''.join('-' if i % 2 == 0 else '+' for i in range(n))
    t = 0
    mn = 0
    for i in s:
        if i == '-':
            t -= 1

        else:
            t += 1
        mn = min(mn, t)
    # print(-mn + t)
    pass
if __name__ == "__main__":
    main(10)