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
    # 这里原代码应为范围 m 而非 n，但 fu 中只对列旋转，不使用 m，
    # 并且只操作长度为 n 的行，因此保持原有结构，外层循环范围使用 n。
    for _ in range(n):
        A[0] = A[0][1:] + A[0][:1]
        for _ in range(n):
            A[1] = A[1][1:] + A[1][:1]
            for _ in range(n):
                A[2] = A[2][1:] + A[2][:1]
                for _ in range(n):
                    A[3] = A[3][1:] + A[3][:1]
                    cur_ans = maxsa(A, n)
                    answer = max(answer, cur_ans)
    return answer

def main(n):
    """
    规模参数 n：
      - 矩阵维度为 n x m，其中 m = n（可根据需要修改生成策略）
      - 随机生成一个 A（n x m），元素为 0~99 的整数
      - 按原逻辑选出 4 列构成 S（4 x n），再调用 fu(S, n)
    """
    # 生成测试数据：设 m = n，可按需要修改
    m = n
    A = [[random.randint(0, 99) for _ in range(m)] for _ in range(n)]

    # 按原代码逻辑选择最多 4 列
    inds = [-1, -1, -1, -1]
    maxs = [0, 0, 0, 0]

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
    # 示例调用：n=4
    main(4)