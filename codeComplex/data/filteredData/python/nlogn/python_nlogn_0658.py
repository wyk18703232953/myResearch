def main(n):
    # Generate deterministic input of size n
    # Original input:
    # n
    # A[1..n]
    #
    # Here we define A[i] = (i % 3) + 1 to ensure values >=1 and some variety.
    if n <= 0:
        return
    A = [0] + [(i % 3) + 1 for i in range(1, n + 1)]

    vec = []
    for i in range(1, n + 1):
        vec = vec + [[A[i], i]]
    list.sort(vec)
    list.reverse(vec)

    if vec[0][0] == 1:
        # print("NO")
        pass
        return

    dia = 0
    path = [vec[0][1]]
    ans = []
    bol, col, idx = 1, 1, 0
    for i in vec[1:]:
        if i[0] != 1:
            ans = ans + [[path[-1], i[1]]]
            dia = dia + 1
            A[path[-1]] = A[path[-1]] - 1
            path += [i[1]]
            A[path[-1]] = A[path[-1]] - 1

        else:
            if col == 1:
                dia = dia + 1
                col = 0
                A[path[0]] -= 1
                ans = ans + [[path[0], i[1]]]
            elif bol == 1:
                dia = dia + 1
                bol = 0
                A[path[-1]] -= 1
                ans = ans + [[path[-1], i[1]]]

            else:
                while idx < len(path) and A[path[idx]] == 0:
                    idx = idx + 1
                if idx == len(path):
                    # print("NO")
                    pass
                    return
                A[path[idx]] = A[path[idx]] - 1
                ans = ans + [[path[idx], i[1]]]

    # print("YES", dia)
    pass
    # print(len(ans))
    pass
    for i in ans:
        # print(i[0], i[1])
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)