import random

def maxsa(A, n):
    ans = 0
    for i in range(n):
        cur_maxx = 0
        for j in range(4):
            cur_maxx = max(cur_maxx, A[j][i])
        ans += cur_maxx
    return ans

def fu(A, n):
    answer = 0
    # 固定 A 的四行顺序，只在每一行内部做循环移位
    base_rows = [row[:] for row in A]  # 深拷贝基准行
    for _ in range(n):
        base_rows[0] = base_rows[0][1:] + base_rows[0][:1]
        row0 = base_rows[0][:]
        row1 = base_rows[1][:]
        row2 = base_rows[2][:]
        row3 = base_rows[3][:]
        for _ in range(n):
            row1 = row1[1:] + row1[:1]
            r1 = row1[:]
            r2 = row2[:]
            r3 = row3[:]
            for _ in range(n):
                r2 = r2[1:] + r2[:1]
                rr2 = r2[:]
                rr3 = r3[:]
                for _ in range(n):
                    rr3 = rr3[1:] + rr3[:1]
                    cur_ans = maxsa([row0, r1, rr2, rr3], n)
                    answer = max(answer, cur_ans)
    return answer

def main(n):
    # 生成测试数据：随机矩阵 A (n x m)，m 也取为 n
    m = n
    # 生成 n 行 m 列的随机整数矩阵，值域可自行调整
    A = [[random.randint(0, 100) for _ in range(m)] for _ in range(n)]

    inds = [-1, -1, -1, -1]
    maxs = [0, 0, 0, 0]

    # 在每一列中找最大值，并维护前 4 大的列
    for j in range(m):
        cur_maxs = 0
        for i in range(n):
            cur_maxs = max(cur_maxs, A[i][j])
        maxs.append(cur_maxs)
        inds.append(j)
        ind = 4
        while ind != 0 and maxs[ind] > maxs[ind - 1]:
            inds[ind], inds[ind - 1] = inds[ind - 1], inds[ind]
            maxs[ind], maxs[ind - 1] = maxs[ind - 1], maxs[ind]
            ind -= 1
        maxs.pop()
        inds.pop()

    S = [0] * 4
    for j in range(4):
        if inds[j] != -1:
            S[j] = [row[inds[j]] for row in A]
        else:
            S[j] = [0] * n

    result = fu(S, n)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)