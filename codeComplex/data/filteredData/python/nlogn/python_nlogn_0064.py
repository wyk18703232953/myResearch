def sum_list(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s

def main(n):
    if n <= 0:
        print(0)
        return
    cns = [i % 100 + 1 for i in range(1, n + 1)]
    xs, nm, c = 0, 0, 0
    cns.append(0)
    while xs <= nm and cns:
        m = max(cns)
        cns.remove(m)
        xs += m
        nm = sum_list(cns)
        c += 1
    print(c)

if __name__ == "__main__":
    main(10)