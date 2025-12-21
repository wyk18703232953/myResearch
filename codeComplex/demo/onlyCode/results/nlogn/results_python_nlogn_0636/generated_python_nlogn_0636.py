def main(n):
    import random
    import sys
    m = max(1, n)
    X = [random.randint(1, 10**9) for _ in range(n)]
    Y = []
    for _ in range(m):
        t = random.randint(1, 2)
        if t == 1:
            if random.random() < 0.1:
                Y.append([1, 10**9])
            else:
                Y.append([1, random.randint(1, 10**9 - 1)])
        else:
            Y.append([2, random.randint(1, 10**9)])
    Z = []
    ANS = 0
    for y in Y:
        if y[0] == 1 and y[1] == 10**9:
            ANS += 1
        elif y[0] == 1:
            Z.append(y[1])
    X.sort(reverse=True)
    Z.sort(reverse=True)
    XCOUNT = [0] * n
    i = 0
    j = 0
    l = len(Z)
    X.append(0)
    Z.append(0)
    while i < l + 1 and j < n:
        if Z[i] >= X[j]:
            i += 1
        else:
            XCOUNT[j] = i
            j += 1
    count = n
    XCOUNT.reverse()
    for i in range(n):
        if count > i + XCOUNT[i]:
            count = i + XCOUNT[i]
    return count + ANS

if __name__ == "__main__":
    print(main(10))