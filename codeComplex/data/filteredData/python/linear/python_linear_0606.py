def main(n):
    if n <= 0:
        return
    ans = [(0, 0)]
    for i in range(1, n):
        ans.append((0, i))
        ans.append((i, 0))
        ans.append((0, -i))
        ans.append((-i, 0))
    for i in range(min(n, len(ans))):
        print(str(ans[i][0]) + ' ' + str(ans[i][1]))


if __name__ == "__main__":
    main(10)