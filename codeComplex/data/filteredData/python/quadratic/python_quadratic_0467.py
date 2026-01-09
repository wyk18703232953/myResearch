from itertools import groupby

def main(n):
    # Deterministic generation of l and r based on n
    l = [i % 5 for i in range(n)]
    r = [(n - 1 - i) % 5 for i in range(n)]

    sums = [(a + b, ind) for (ind, (a, b)) in enumerate(zip(l, r))]
    sums.sort()
    answer = [None] * n
    curr_candies = n
    for key, group in groupby(sums, key=lambda i: i[0]):
        for elem in group:
            answer[elem[1]] = curr_candies
        curr_candies -= 1
    tl = []
    for i in range(n):
        cnt = 0
        for j in range(i):
            if answer[j] > answer[i]:
                cnt += 1
        tl.append(cnt)
    tr = []
    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if answer[j] > answer[i]:
                cnt += 1
        tr.append(cnt)
    if tl != l or tr != r:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
        # print(' '.join(map(str, answer)))
        pass
if __name__ == "__main__":
    main(10)