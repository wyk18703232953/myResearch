def main(n):
    N = n
    intervals = []
    for i in range(N):
        x = i * 2 + 1
        w = (i % 5) + 1
        left = x - w
        right = x + w
        intervals.append((left, right))
    intervals.sort(key=lambda x: x[1])

    left = -1000000007
    ans = 0
    for i in range(N):
        if intervals[i][0] >= left:
            ans += 1
            left = intervals[i][1]
    print(ans)


if __name__ == "__main__":
    main(10)