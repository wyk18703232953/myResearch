def main(n):
    k = max(1, min(n, n // 2 + 1))
    lst = []
    for i in range(n):
        a = i + 1
        b = n - i
        lst.append([-a, b])
    lst.sort()
    return lst.count(lst[k - 1])

if __name__ == "__main__":
    print(main(10))