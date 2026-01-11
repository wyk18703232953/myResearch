def main(n):
    # 生成确定性的测试数据 A，长度为 n
    # 使用简单算术构造：A[i] = (i * 3 + 1) % (n + 7)
    A = [(i * 3 + 1) % (n + 7) for i in range(n)]

    B = A.copy()
    B.sort()
    c = 0
    for i in range(n):
        c = c + 1 if A[i] != B[i] else c
    # print("YES" if c <= 2 else "NO")
    pass
if __name__ == "__main__":
    main(10)