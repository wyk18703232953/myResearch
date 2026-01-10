def main(n):
    a = []
    # Generate n intervals deterministically
    # Example pattern: intervals [2*i, 2*i + 2]
    for i in range(n):
        x = 2 * i
        y = 2 * i + 2
        a.append((x, 0))
        a.append((y, 1))
    a.sort()
    ans, s = [0] * n, []
    for x, y in a:
        if y:
            ans[len(s) - 1] += x - s[-1][0] + 1 - s[-1][1]
            z = s.pop()
            if s:
                s[-1][1] += (x - z[0] + 1)
        else:
            s.append([x, 0])
    print(*ans)


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)