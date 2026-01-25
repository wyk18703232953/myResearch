from collections import namedtuple

def main(n):
    vertex = namedtuple('vertex', ['degree', 'id'])
    a, b, c = [], [], 0

    # Deterministically generate degrees list rr of length n
    # Example pattern: rr[i] cycles through 0..3
    rr = [(i % 4) for i in range(n)]

    for i in range(n):
        tmp = rr[i]
        v = vertex(tmp, i + 1)
        if tmp > 1:
            a.append(v)
        else:
            b.append(v)
        c += tmp

    if c < (n - 1) * 2:
        print('NO')
    else:
        if len(a) == 0:
            if n >= 2:
                print('YES 1')
                print('1 2')
            else:
                print('NO')
        else:
            print('YES', len(a) - 1 + min(2, len(b)))
            print(n - 1)
            for i in range(len(a)):
                if i == 0:
                    continue
                print(a[i - 1].id, a[i].id)
            if len(b) > 0:
                print(b[0].id, a[0].id)
            if len(b) > 1:
                print(b[1].id, a[-1].id)
            j = 2
            for i in range(len(a)):
                if j >= len(b):
                    yes = 1
                    break
                k = a[i].degree - 2
                yes = 0
                for t in range(k):
                    if j >= len(b):
                        yes = 1
                        break
                    print(a[i].id, b[j].id)
                    j += 1
                if yes == 1:
                    break

if __name__ == "__main__":
    # Example deterministic calls for experimentation
    main(1)
    main(5)
    main(10)