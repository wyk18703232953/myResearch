from itertools import combinations

def main(n):
    # Interpret n as the number of elements in lst
    if n < 2:
        print(0)
        return

    p = n  # allow all subset sizes from 2 up to n
    minn = n          # lower bound for sum
    maxn = n * (n + 1) // 2  # upper bound for sum (sum of 1..n)
    dif = max(1, n // 10)    # minimum difference between max and min

    lst = [i + 1 for i in range(n)]

    c = 0
    for i in range(2, p + 1):
        for j in combinations(lst, i):
            if (maxn >= sum(j) >= minn) and (max(j) - min(j) >= dif):
                c += 1
    print(c)

if __name__ == "__main__":
    main(10)