def main(n):
    acc = {0: 0}
    ps = [i + 2 for i in range(n)]
    cs = [1 for _ in range(n)]
    for p, c in zip(ps, cs):
        adds = []
        for b, u in acc.items():
            a = p
            bb = b
            while bb:
                a, bb = bb, a % bb
            adds.append((a, u + c))
        for a, u in adds:
            acc[a] = min(u, acc.get(a, 1000000000))
    return acc.get(1, -1)


if __name__ == '__main__':
    print(main(5))