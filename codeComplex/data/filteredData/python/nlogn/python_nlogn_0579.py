def solve(N):
    ans = []

    end = N
    fac = 1

    while end >= 1:
        if end == 1:
            ans.append(fac)
            end = 0
            break

        if end == 2:
            ans.append(fac)
            ans.append(fac * 2)
            end = 0
            break

        if end == 3:
            ans.append(fac)
            ans.append(fac)
            ans.append(fac * 3)
            end = 0
            break

        ans.extend([fac] * ((end + 1) // 2))
        end //= 2
        fac *= 2

    return ans


def main(n):
    N = n
    result = solve(N)
    print(*result)


if __name__ == "__main__":
    main(10)