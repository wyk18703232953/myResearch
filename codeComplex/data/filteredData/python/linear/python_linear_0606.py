def main(n):
    if n <= 0:
        return
    ans = [(0, 0)]
    for i in range(1, n):
        ans.append((0, i))
        ans.append((i, 0))
        ans.append((0, -i))
        ans.append((-i, 0))
    limit = min(n, len(ans))
    output_lines = []
    for i in range(limit):
        output_lines.append(str(ans[i][0]) + ' ' + str(ans[i][1]))
    # print("\n".join(output_lines))
    pass
if __name__ == "__main__":
    main(10)