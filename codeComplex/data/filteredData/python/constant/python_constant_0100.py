def main(n):
    t = n
    ans = []
    for j in range(t):
        a = j + 2
        b = 2 * j + 3
        k = 0
        while a > 0 and b > 0:
            if a >= b:
                k += a // b
                a %= b

            else:
                k += b // a
                b %= a
        ans.append(str(k))
    # print("\n".join(ans))
    pass
if __name__ == "__main__":
    main(10)