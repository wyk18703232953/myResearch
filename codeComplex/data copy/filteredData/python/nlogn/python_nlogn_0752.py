def solve(n, a):
    a = sorted(a)
    if n == 1:
        return a[0] > 0 and a[0] % 2 == 1
    same_count = 0
    for i in range(n - 1):
        if a[i] == a[i + 1] == 0:
            return False
        if i < n - 2 and a[i] + 1 == a[i + 1] == a[i + 2]:
            return False
        if a[i] == a[i + 1]:
            same_count += 1
    if same_count > 1:
        return False
    return (sum(a) - n * (n - 1) // 2) % 2 == 1


def main(n):
    if n <= 0:
        return
    a = [i % (n + 1) for i in range(n)]
    r = solve(n, a)
    if r:
        # print('sjfnb')
        pass

    else:
        # print('cslnb')
        pass
if __name__ == "__main__":
    main(5)