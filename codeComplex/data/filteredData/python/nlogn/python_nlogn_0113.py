def main(n):
    # 生成长度为 n 的确定性数组 A
    A = [(i * 3 + 7) % (n + 5) for i in range(n)]

    B = A.copy()
    B.sort()
    c = 0
    for i in range(n):
        a = A[i]
        b = B[i]
        if a == b:
            continue
        else:
            c += 1
    if c == 0 or c == 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(10)