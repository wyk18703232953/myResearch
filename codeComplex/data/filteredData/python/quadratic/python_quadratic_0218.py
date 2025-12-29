import random

def main(n):
    # 生成测试数据：n 行，m 列的 0/1 字符串矩阵
    # 这里令 m 与 n 相同，你也可以按需修改生成规则
    m = n
    a = []
    for _ in range(n):
        row = ''.join(random.choice('01') for _ in range(m))
        a.append(row)

    ans = "NO"
    count = [0] * m

    # 统计每一列中 '1' 的数量
    for i in range(n):
        for j in range(m):
            if a[i][j] == '1':
                count[j] += 1

    # 检查是否存在一行，删除它后每一列仍至少有一个 '1'
    for i in range(n):
        ans = "YES"
        for j in range(m):
            if count[j] == 1 and a[i][j] == '1':
                ans = "NO"
                break
        if ans == "YES":
            break

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(5)，可以根据需要修改 n
    main(5)