def main(n):
    # Interpret n as the length of the list
    # Deterministically generate the list l of length n
    # Example pattern: l[i] = (i * 2) % max(1, n//2)
    if n <= 0:
        print("NO")
        return

    mod_base = max(1, n // 2)
    l = [(i * 2) % mod_base for i in range(n)]

    s = list(set(l))
    s.sort()

    if len(s) > 1:
        ans = s[1]
    else:
        ans = 'NO'

    print(ans)


if __name__ == "__main__":
    main(10)