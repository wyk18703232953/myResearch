def main(n):
    # n: number of items
    # Deterministic generation of capacity and items
    # Capacity grows roughly with n to keep behavior meaningful
    capacity = n * (n // 2 + 1)

    a = []
    for i in range(n):
        # Deterministic (x, y) generation
        # x increases with i, y is some function of i to create variation
        x = (i + 1) * 3
        y = (i * i + 2) // 3
        a.append((x, y))

    a.sort(key=lambda x: max(0, x[0] - x[1]))

    current_sum = 0
    for x in a:
        current_sum += x[0]
    i = n - 1
    ans = 0

    while i >= 0 and current_sum > capacity:
        ans += 1
        current_sum -= max(0, a[i][0] - a[i][1])
        i -= 1

    if current_sum <= capacity:
        # print(ans)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)