from itertools import combinations

def main(n):
    if n < 1:
        print(0)
        return
    a = [i for i in range(1, n + 1)]
    l = n
    r = 2 * n
    x = max(1, n // 4)
    c = 0
    for i in range(1, n + 1):
        for j in combinations(a, i):
            if l <= sum(j) <= r and max(j) - min(j) >= x:
                c += 1
    print(c)

if __name__ == "__main__":
    main(5)