import random

def main(n):
    # 生成测试数据：4 个 n×n 的 0/1 矩阵
    parts = []
    for _ in range(4):
        part = []
        for _ in range(n):
            row = [random.randint(0, 1) for _ in range(n)]
            part.append(row)
        parts.append(part)

    processed_parts = []
    for part in parts:
        dt1 = 0
        exp = 1

        # 第一种起始模式
        for h in range(n):
            for w in range(n):
                if part[h][w] != exp:
                    dt1 += 1
                exp = (exp + 1) % 2

        dt2 = 0
        # 注意：第二种模式从当前 exp 继续，与原代码保持一致
        for h in range(n):
            for w in range(n):
                if part[h][w] != exp:
                    dt2 += 1
                exp = (exp + 1) % 2

        processed_parts.append([dt1, dt2])

    ans = n * n * 4

    for i in range(3):
        for j in range(i + 1, 4):
            a = 0
            for k, part in enumerate(processed_parts):
                if k == i or k == j:
                    a += part[0]
                else:
                    a += part[1]
            ans = min(ans, a)

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(3)，实际使用时请根据需要修改 n
    main(3)