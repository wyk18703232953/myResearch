def main(n):
    # Deterministically generate input data based on n
    # ai: 1..n repeated/cycled
    ai = [(i % n) + 1 for i in range(n)]
    # bi: reverse of 1..n, cycled to length n
    base_b = list(range(n, 0, -1))
    bi = [base_b[i % n] for i in range(n)]

    ai2 = [0] * (n + 1)
    n2 = 0
    output = []
    for i in range(n):
        num = 0
        if ai2[bi[i]] != 1:
            for j in range(n2, n):
                ai2[ai[j]] = 1
                if ai[j] == bi[i]:
                    num = j + 1 - n2
                    n2 = j + 1
                    break
        output.append(str(num))
    # print(" ".join(output))
    pass
if __name__ == "__main__":
    main(10)