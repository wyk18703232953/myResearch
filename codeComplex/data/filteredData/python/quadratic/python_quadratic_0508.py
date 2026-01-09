def solve(H, W, A):
    visited = [bytearray(W) for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if A[y][x] == '.' or visited[y][x]:
                continue

            for dx, dy in [
                (0, 0), (-1, 0), (-2, 0),
                (0, -1), (-2, -1),
                (0, -2), (-1, -2), (-2, -2)
            ]:
                tx = x + dx
                ty = y + dy
                if tx < 0 or ty < 0 or tx + 2 >= W or ty + 2 >= H:
                    continue
                bad = False
                for ex, ey in [
                    (0, 0), (1, 0), (2, 0),
                    (0, 1), (2, 1),
                    (0, 2), (1, 2), (2, 2)
                ]:
                    nx = tx + ex
                    ny = ty + ey
                    if A[ny][nx] == '.':
                        bad = True
                        break
                if bad:
                    continue

                for ex, ey in [
                    (0, 0), (1, 0), (2, 0),
                    (0, 1), (2, 1),
                    (0, 2), (1, 2), (2, 2)
                ]:
                    nx = tx + ex
                    ny = ty + ey
                    visited[ny][nx] = 1

                assert visited[ny][nx] == 1
                break

            if visited[y][x] == 0:
                return False

    return True


def main(n):
    # Map n to grid size: choose H = W = max(1, n)
    H = max(1, n)
    W = max(1, n)

    # Deterministically generate grid A of size H x W
    # Pattern: a mix of '#' and '.' based on (row, col) indices
    A = []
    for y in range(H):
        row = []
        for x in range(W):
            # Simple deterministic pattern
            # Densely place '#' so 3x3 detection has work to do
            if (x + 2 * y) % 3 == 0:
                row.append('#')

            else:
                row.append('.')
        A.append(''.join(row))

    res = solve(H, W, A)
    # print('YES' if res else 'NO')
    pass
if __name__ == "__main__":
    main(10)