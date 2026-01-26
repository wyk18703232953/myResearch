def main(n):
    # Interpret n as the grid size: n x n grid
    # m will also be n to keep structure similar to original
    from collections import deque

    # Ensure minimum meaningful size
    if n < 1:
        n = 1
    m = n

    # Directions (same as original)
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    # Define number of starting points k deterministically
    # Use up to n starting points but at least 1
    k = max(1, n // 2)

    # Generate deterministic starting coordinates a of length 2*k
    # Coordinates are in range [1, n]
    a = []
    for i in range(k):
        x = (i % n) + 1
        y = ((i * 2) % n) + 1
        a.append(x)
        a.append(y)

    # Initialize grid v with border of zeros and inside ones
    v = [[1] * (m + 2) for _ in range(n + 2)]
    for i in range(m + 2):
        v[0][i] = 0
        v[-1][i] = 0
    for i in range(n + 2):
        v[i][0] = 0
        v[i][-1] = 0

    # Initialize queue with starting points and mark them as 0
    q = deque()
    for i in range(0, 2 * k, 2):
        x0, y0 = a[i], a[i + 1]
        # Clip coordinates to valid inner region in case n is very small
        if 1 <= x0 <= n and 1 <= y0 <= m and v[x0][y0]:
            q.append((x0, y0))
            v[x0][y0] = 0

    # If all starting points were out of range (should not happen with our generation),
    # we add a default one
    if not q:
        q.append((1, 1))
        v[1][1] = 0

    # BFS as in original code
    while True:
        x, y = q.popleft()
        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if v[xx][yy]:
                q.append((xx, yy))
                v[xx][yy] = 0
        if not q:
            # Original program wrote x, y to output.txt
            # For experiment purposes, just print to stdout
            # print(x, y)
            pass
            break


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)