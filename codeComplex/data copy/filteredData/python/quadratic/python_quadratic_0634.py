def main(n):
    if n <= 0:
        return 0

    # 构造确定性的测试数据：A[i] = i + 1
    A = [i + 1 for i in range(n)]

    A.sort()

    ANS = [0] * n
    NOW = 1

    for i in range(n):
        if ANS[i] == 0:
            ANS[i] = NOW
            for j in range(i, n):
                if A[j] % A[i] == 0 and ANS[j] == 0:
                    ANS[j] = NOW
            NOW += 1

    result = max(ANS)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)