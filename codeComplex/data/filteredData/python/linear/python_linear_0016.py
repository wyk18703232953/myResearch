def f(n):
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1
    return True

def core_logic(n, k):
    a = []
    x = 0
    for i in range(2, n + 1):
        if f(i):
            a.append(i)
    for i in range(len(a) - 2):
        if a[i] + a[i + 1] + 1 in a:
            x += 1
    if x >= k:
        return 'YES'

    else:
        return 'NO'

def main(n):
    if n < 2:
        n_effective = 2

    else:
        n_effective = n
    k = max(1, n_effective // 10)
    result = core_logic(n_effective, k)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)