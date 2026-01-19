from math import log

def solve(n, q, queries):
    x = int(log(n + 1, 2))
    root = 1 << (x - 1)
    outputs = []
    for u, s in queries:
        if u < root:
            pos = 'L'
        elif u > root:
            pos = 'R'
        else:
            pos = 'U'

        s1 = bin(u)[2:]
        s1 = '0' * (x - len(s1)) + s1
        s1 = list(s1)
        for j in s:
            for k in range(x - 1, -1, -1):
                if s1[k] == '1':
                    f = k
                    break
            if j == 'L':
                if f == x - 1:
                    continue
                s1[f] = '0'
                s1[f + 1] = '1'
            elif j == 'R':
                if f == x - 1:
                    continue
                s1[f + 1] = '1'
            else:
                if f == 0:
                    continue
                if s1[f - 1] == '1':
                    s1[f] = '0'
                else:
                    s1[f - 1] = '1'
                    s1[f] = '0'
        s1 = "".join(s1)
        outputs.append(int(s1, 2))
    return outputs

def main(n):
    if n < 2:
        n = 2
    q = n
    queries = []
    for i in range(1, q + 1):
        u = (i % (n - 1)) + 1
        if i % 3 == 1:
            s = "L" * (i % 5)
        elif i % 3 == 2:
            s = "R" * (i % 5)
        else:
            length = i % 5
            s = "".join("L" if (k % 2 == 0) else "R" for k in range(length))
        queries.append((u, s))
    results = solve(n, q, queries)
    for val in results:
        print(val)

if __name__ == "__main__":
    main(8)