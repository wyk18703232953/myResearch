import heapq

def main(n):
    w = [(i * 2 + 3) % (10 * n + 7) + 1 for i in range(n)]
    s = []
    for i in range(1, 2 * n + 1):
        s.append('0' if i % 2 == 1 else '1')
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
            heapq.heappush(ones, [-l[0], l[1]])
        else:
            l = ones[0]
            heapq.heappop(ones)
            res.append(l[1])
    res_str = ' '.join(str(i) for i in res)
    print(res_str)


if __name__ == "__main__":
    main(5)