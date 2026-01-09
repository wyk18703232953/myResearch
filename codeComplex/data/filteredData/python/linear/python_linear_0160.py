def main(n):
    # Deterministically generate input data E of size n
    # Here we generate a sequence with repeating pattern using modulo
    E = [i % (max(1, n // 3)) for i in range(n)]

    D = dict()
    for e in E:
        D[e] = D.get(e, 0) + 1
    for e in E:
        # print(D[e])
        pass
if __name__ == "__main__":
    main(10)