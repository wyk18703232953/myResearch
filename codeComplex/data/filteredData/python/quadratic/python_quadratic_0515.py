import random

def main(n):
    # 这里选择一个与 n 相关的 m，可以按需修改生成规则
    m = max(3, n)  # 保证至少为 3，避免原逻辑中的 n-2, m-2 出现负数

    # 生成测试数据：n 行 m 列，只包含 '.' 或 '#'
    # 你可以改成任何需要的生成逻辑，例如保证一定有 3x3 的全 '#'
    l = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append(random.choice(['.', '#']))
        l.append(row)

    # 原代码逻辑开始
    ans = []
    for i in range(n):
        ans.append([])
        for _ in range(m):
            ans[-1].append(".")

    for i in range(n - 2):
        for j in range(m - 2):
            if l[i][j] == "#":
                if (
                    l[i][j] == l[i][j + 1] and
                    l[i][j] == l[i][j + 2] and
                    l[i][j] == l[i + 1][j] and
                    l[i][j] == l[i + 1][j + 2] and
                    l[i][j] == l[i + 2][j] and
                    l[i][j] == l[i + 2][j + 1] and
                    l[i][j] == l[i + 2][j + 2]
                ):
                    ans[i][j] = "#"
                    ans[i][j + 1] = "#"
                    ans[i][j + 2] = "#"
                    ans[i + 1][j] = "#"
                    ans[i + 1][j + 2] = "#"
                    ans[i + 2][j] = "#"
                    ans[i + 2][j + 1] = "#"
                    ans[i + 2][j + 2] = "#"

    flag = True
    for i in range(n):
        for j in range(m):
            if l[i][j] != ans[i][j]:
                flag = False
                break
        if flag is False:
            break

    if flag is True:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5)，你可以根据需要修改或删除
    main(5)