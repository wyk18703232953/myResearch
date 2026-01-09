def main(n):
    # Generate two digit-strings of length n deterministically
    # Map original input structure: each line is a string of digits, read as list(map(int, input().rstrip()))
    # Here we construct them from n using simple arithmetic patterns.
    s1 = "".join(str((i * 7 + 3) % 10) for i in range(n))
    s2 = "".join(str((i * 5 + 1) % 10) for i in range(n))

    a = list(map(int, s1))
    b = list(map(int, s2))
    ans, la, lb = [], len(a), len(b)

    if la != lb:
        # print(*sorted(a, reverse=True), sep="")
        pass

    else:
        i = 0
        while i < lb:
            if b[i] in a:
                ans.append(b[i])
                a.remove(b[i])
                i += 1

            else:
                while i > -1:
                    ma = -1
                    for j in a:
                        if j < b[i]:
                            ma = max(ma, j)
                    if ma != -1:
                        ans.append(ma)
                        a.remove(ma)
                        break
                    i -= 1
                    a.append(ans.pop())
                a.sort()
                while a:
                    ans.append(a.pop())
                break
        # print(*ans, sep="")
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(10)