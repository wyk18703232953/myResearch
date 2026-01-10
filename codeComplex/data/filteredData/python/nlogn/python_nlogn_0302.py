import heapq

def main(n):
    w = [i + 1 for i in range(n)]
    s = []
    for i in range(n):
        s.append('0')
        s.append('1')
    s = ''.join(s)

    idx = []
    for i in range(n):
        idx.append((w[i], i + 1))

    idx.sort()
    heapq.heapify(idx)
    ones = []
    heapq.heapify(ones)
    res = []
    for i in range(2 * n):
        if s[i] == '0':
            l = idx[0]
            heapq.heappop(idx)
            res.append(l[1])
            heapq.heapush(ones, [-l[0], l[1]])
        else:
            l = ones[0]
            heapq.heappop(ones)
            res.append(l[1])
    res = ' '.join(str(i) for i in res)
    print(res)

if __name__ == "__main__":
    main(10)