import random

def main(n):
    # 生成测试数据：n, m, k 和数组 A
    # 这里选择一种简单的生成方式，可按需要自行修改
    m = max(1, n // 3)         # 保证 1 <= m <= n
    k = random.randint(0, 10)  # 任意非负整数罚值
    A = [random.randint(-10, 10) for _ in range(n)]

    glans = 0
    for s in range(m):
        B = []
        f = s
        su = 0
        sus = 0
        for i in range(s, n):
            su += A[i]
            sus = max(sus, su)
            if (i + 1) % m == s:
                B.append(sus - k)
                B.append(su - sus)
                su = 0
                sus = 0
                f = i + 1
        dob = 0
        klol = 0
        for j in range(f, n):
            dob += A[j]
            klol = max(klol, dob - k)
        B = [0] + B + [klol]
        for i in range(1, len(B)):
            B[i] += B[i - 1]
        cnt = -10 ** 10
        ans = [0, 0]
        minsum = 10 ** 10
        candidat = 0
        for i in range(len(B)):
            if B[i] - minsum > cnt:
                cnt = B[i] - minsum
                ans[1] = i
                ans[0] = candidat
            if B[i] <= minsum:
                minsum = B[i]
                candidat = i
        glans = max(glans, B[ans[1]] - B[ans[0]])
    print(glans)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需修改 n
    main(10)