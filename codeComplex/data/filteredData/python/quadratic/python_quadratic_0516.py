import random

def main(n: int) -> None:
    # 生成一个 n 行 m 列的随机网格，其中 '.' / '#' 随机分布
    m = n  # 这里简单取 m = n，如需不同可自行修改
    a = []
    for _ in range(n):
        row = ''.join(random.choice(['.', '#']) for _ in range(m))
        a.append(row)

    for i in range(n):
        for j in range(m):
            if a[i][j] == '.':
                continue
            if i >= 2 and j >= 2:
                if (
                    a[i - 2][j - 2] == '#' and a[i - 2][j - 1] == '#' and a[i - 2][j] == '#'
                    and a[i - 1][j] == '#' and a[i - 1][j - 2] == '#'
                    and a[i][j - 1] == '#' and a[i][j - 2] == '#'
                ):
                    continue
            if (
                i >= 1 and i <= n - 2 and j >= 2
                and a[i - 1][j - 2] == '#' and a[i - 1][j - 1] == '#' and a[i - 1][j] == '#'
                and a[i][j - 2] == '#' and a[i + 1][j - 2] == '#'
                and a[i + 1][j - 1] == '#' and a[i + 1][j] == '#'
            ):
                continue
            if (
                i <= n - 3 and j >= 2
                and a[i][j - 1] == '#' and a[i][j - 2] == '#'
                and a[i + 1][j] == '#' and a[i + 1][j - 2] == '#'
                and a[i + 2][j] == '#' and a[i + 2][j - 1] == '#' and a[i + 2][j - 2] == '#'
            ):
                continue
            if (
                i <= n - 3 and j >= 1 and j <= m - 2
                and a[i][j - 1] == '#' and a[i][j + 1] == '#'
                and a[i + 1][j - 1] == '#' and a[i + 1][j + 1] == '#'
                and a[i + 2][j] == '#' and a[i + 2][j - 1] == '#' and a[i + 2][j + 1] == '#'
            ):
                continue
            if (
                i <= n - 3 and j <= m - 3
                and a[i][j + 1] == '#' and a[i][j + 2] == '#'
                and a[i + 1][j] == '#' and a[i + 1][j + 2] == '#'
                and a[i + 2][j] == '#' and a[i + 2][j + 1] == '#' and a[i + 2][j + 2] == '#'
            ):
                continue
            if (
                i <= n - 2 and i >= 1 and j <= m - 3
                and a[i - 1][j] == '#' and a[i - 1][j + 1] == '#' and a[i - 1][j + 2] == '#'
                and a[i][j + 2] == '#' and a[i + 1][j] == '#' and a[i + 1][j + 1] == '#' and a[i + 1][j + 2] == '#'
            ):
                continue
            if (
                i >= 2 and j <= m - 3
                and a[i - 2][j] == '#' and a[i - 2][j + 1] == '#' and a[i - 2][j + 2] == '#'
                and a[i - 1][j] == '#' and a[i - 1][j + 2] == '#'
                and a[i][j + 1] == '#' and a[i][j + 2] == '#'
            ):
                continue
            if (
                i >= 2 and j <= m - 2 and j >= 1
                and a[i - 2][j - 1] == '#' and a[i - 2][j] == '#' and a[i - 2][j + 1] == '#'
                and a[i - 1][j - 1] == '#' and a[i - 1][j + 1] == '#'
                and a[i][j - 1] == '#' and a[i][j + 1] == '#'
            ):
                continue
            print('NO')
            return
    print('YES')


if __name__ == "__main__":
    # 示例调用，n 可根据需要修改
    main(5)