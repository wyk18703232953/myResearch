def main(n):
    # Deterministically generate three points (ax, ay), (bx, by), (cx, cy)
    # Make coordinates scale with n so input size/coordinate magnitude ~ O(n)
    ax = 0
    ay = 0
    bx = n
    by = n // 2
    cx = 2 * n
    cy = n

    # Original logic
    if ax > bx:
        ax, bx = bx, ax
        ay, by = by, ay
    if ax > cx:
        ax, cx = cx, ax
        ay, cy = cy, ay
    if bx > cx:
        bx, cx = cx, bx
        by, cy = cy, by

    ans = []
    for i in range(min(ay, by, cy), max(ay, by, cy) + 1):
        ans.append([bx, i])
    for i in range(ax, bx):
        ans.append([i, ay])
    for i in range(bx + 1, cx + 1):
        ans.append([i, cy])

    # print(len(ans))
    pass
    for x, y in ans:
        # print(x, y)
        pass
if __name__ == "__main__":
    main(10)