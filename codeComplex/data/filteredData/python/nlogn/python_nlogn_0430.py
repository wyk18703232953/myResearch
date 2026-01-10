def solve(a):
    count = 0
    mp = Counter(a)
    for i in range(len(a)):
        flag = 0
        for j in range(31):
            x = (1 << j) - a[i]
            if (x in mp) and (x == a[i] and mp[x] > 1):
                flag = 1
                break
            elif (x in mp) and (x != a[i] and mp[x] > 0):
                flag = 1
                break
        if flag == 0:
            count += 1
    return count


from collections import Counter


def main(n):
    # n is the length of the array
    # deterministically generate test data of size n
    # example pattern: a[i] = (i * 3) % (n + 7)
    a = [(i * 3) % (n + 7) for i in range(n)]
    res = solve(a)
    print(res)


if __name__ == "__main__":
    main(10)