D = False

def hash_cell(r, c):
    return str(r) + "-" + str(c)

def sol(R, C, m):
    count = 0
    for line in m:
        count += line.count("#")

    if D:
        print("Count:", count)

    lookup = {}
    for r in range(1, R - 1):
        for c in range(1, C - 1):

            if D:
                print("  row,col:", r, c)

            offset = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 1),
                      (1, -1), (1, 0), (1, 1)]
            lst = []
            fail = False

            # ensure all 8 adjacent cells are '#'
            for o in offset:
                cell = (r + o[0], c + o[1])
                if D:
                    print("  cell:", cell, m[cell[0]][cell[1]])
                h = hash_cell(cell[0], cell[1])

                if m[cell[0]][cell[1]] == "#":
                    if h not in lookup:
                        lst.append(h)
                else:
                    fail = True
                    break

            if not fail:
                for item in lst:
                    lookup[item] = True
                count -= len(lst)

    return "YES" if count == 0 else "NO"


def main(n):
    # 生成一个 n x n 的测试矩阵
    # 规则：
    # - 边界全部为 '.'
    # - 内部按简单模式放置 '#'
    #   对于所有以 (r,c) 为中心满足 (r + c) % 3 == 0 的 3x3 区域，
    #   将其 8 个邻居设为 '#'
    if n < 3:
        # 小于 3 行列时，肯定没有被 3x3 覆盖的 '#'
        R = C = n
        m = ["." * C for _ in range(R)]
        return sol(R, C, m)

    R = C = n
    grid = [["." for _ in range(C)] for _ in range(R)]

    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),           (0, 1),
               (1, -1),  (1, 0),  (1, 1)]

    for r in range(1, R - 1):
        for c in range(1, C - 1):
            if (r + c) % 3 == 0:
                for dr, dc in offsets:
                    rr, cc = r + dr, c + dc
                    grid[rr][cc] = "#"

    m = ["".join(row) for row in grid]
    return sol(R, C, m)


if __name__ == "__main__":
    # 示例：调用 main(10) 并打印结果
    print(main(10))