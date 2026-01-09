def main(n):
    A = [i + 1 for i in range(n)]
    A.sort()
    B = [0] * n
    ans = 0
    for i in range(n):
        if B[i] == 0:
            ans += 1
            B[i] = 1
            for j in range(n):
                if A[j] % A[i] == 0:
                    B[j] = 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)