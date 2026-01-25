def count(audrey, imba, banget):
    return (imba - audrey - 1) % (banget - 1)

def simulate(n, q, L, queries):
    maxi = max(L)
    indexmax = L.index(maxi)
    P = []
    for _ in range(indexmax):
        P.append((L[0], L[1]))
        if L[0] < L[1]:
            L.append(L.pop(0))
        else:
            L.append(L.pop(1))
    Y = tuple(L[1:])
    outputs = []
    for m in queries:
        if m <= indexmax:
            outputs.append(f"{P[m-1][0]} {P[m-1][1]}")
        else:
            outputs.append(f"{maxi} {Y[count(indexmax, m, n)]}")
    return outputs

def main(n):
    if n < 2:
        n = 2
    q = n
    L = [i + 1 for i in range(n)]
    queries = [i + 1 for i in range(q)]
    results = simulate(n, q, L, queries)
    for line in results:
        print(line)

if __name__ == "__main__":
    main(5)