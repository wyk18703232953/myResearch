from itertools import accumulate

def main(n):
    # Interpret n as: array length; choose fixed small m and k relative to n
    if n <= 0:
        return
    m = max(1, n // 3)  # number of groups
    k = max(1, n // 5)  # decrement value

    # Deterministic construction of array a of length n
    # For variability, use simple arithmetic pattern
    a = [(i * 2 + (i % 3) - (i // 2)) for i in range(n)]

    als = []
    for i in range(m):
        ls = a[:]
        for j in range(n):
            if j % m == i:
                ls[j] -= k
        als.append(list(accumulate(ls)))
    ans = 0
    for i in range(m):
        ls = als[i]
        mn = 0
        anstmp = 0
        for j in range(n):
            if mn > ls[j]:
                mn = ls[j]
            if j % m == i:
                anstmp = max(anstmp, ls[j] - mn)
        ans = max(ans, anstmp)
    # print(ans)
    pass
if __name__ == "__main__":
    # Example scale; adjust n to run time-complexity experiments
    main(1000)