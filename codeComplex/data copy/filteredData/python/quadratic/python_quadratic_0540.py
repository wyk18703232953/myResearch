from collections import namedtuple

vertex = namedtuple('vertex', ['degree', 'id'])

def main(n):
    # Deterministically generate input scale and data
    n = max(1, int(n))
    rr = [(i % 4) + 1 for i in range(n)]

    a, b, c = [], [], 0

    for i in range(n):
        if rr[i] > 1:
            a.append(vertex(rr[i], i + 1))

        else:
            b.append(vertex(rr[i], i + 1))
        c += rr[i]

    if c < (n - 1) * 2:
        # print('NO')
        pass

    else:
        # print('YES', len(a) - 1 + min(2, len(b)))
        pass
        # print(n - 1)
        pass
        for i in range(1, len(a)):
            # print(a[i - 1].id, a[i].id)
            pass
        if len(b) > 0:
            # print(b[0].id, a[0].id)
            pass
        if len(b) > 1:
            # print(b[1].id, a[-1].id)
            pass
        j, yes = 2, 0
        for i in range(len(a)):
            k = a[i].degree - 2
            for t in range(k):
                if j >= len(b):
                    yes = 1
                    break
                # print(a[i].id, b[j].id)
                pass
                j += 1
            if yes == 1:
                break

if __name__ == "__main__":
    main(10)