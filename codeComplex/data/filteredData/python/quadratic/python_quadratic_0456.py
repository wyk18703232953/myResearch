def main(n):
    from operator import itemgetter

    if n <= 0:
        return

    # Deterministic generation of ai based on n
    # Example: positive integers with some variation
    ai = [(i * 2 + 3) % (2 * n + 1) + 1 for i in range(n)]

    ai2 = [[ai[i], i] for i in range(n)]
    answer = [0] * n
    ai2.sort(key=itemgetter(0))

    answer[ai2[0][1]] = 1
    answer[ai2[-1][1]] = 0

    for i in range(n - 2, 0, -1):
        if ai2[i][0] == 0:
            continue
        num = ai2[i][1] % ai2[i][0]
        for j in range(num, n, ai2[i][0]):
            if ai[j] > ai2[i][0] and answer[j] == 0:
                answer[ai2[i][1]] = 1
                break

    out = []
    for i in range(n):
        if answer[i] == 1:
            out.append("A")

        else:
            out.append("B")
    # print("".join(out))
    pass
if __name__ == "__main__":
    main(10)