
def combine(n, k, w=1, out=[], result=[]):
    if k == 0:
        result.append(out)

    for i in range(w, n + 1):
        new_out = out[:]
        new_out.append(i)
        combine(n, k-1, i+1, new_out)

    return result


def main():

    n, l, r, x = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]

    if n < 2:
        print(0)
        return

    result = None
    for i in range(2, n + 1):
        if i == n:
            result = combine(n, i)
        else:
            combine(n, i)

    for i in range(len(result)):
        comb = result[i]
        for j in range(len(comb)):
            comb[j] = c[comb[j] - 1]

    cnt = 0
    for i in range(len(result)):
        sm = sum(result[i])
        if sm >= l and sm <= r and (max(result[i]) - min(result[i]) >= x):
            cnt += 1

    print(cnt)



if __name__ == '__main__':
    main()


