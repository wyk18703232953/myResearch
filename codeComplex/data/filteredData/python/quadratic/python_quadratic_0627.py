def main(n):
    arr = [(i % 7) + 1 for i in range(1, n + 1)]
    color = [0] * n
    arr.sort()

    ans = 0
    for i in range(n):
        if color[i]:
            continue
        ans += 1
        for j in range(i, n):
            if arr[j] % arr[i] == 0:
                color[j] = ans

    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(10)