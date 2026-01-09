def main(n):
    a = n
    arr = [i % a + 1 for i in range(a)]
    mn = float("inf")
    for i in range(1, a + 1):
        mn = min(mn, arr.count(i))
    # print(mn)
    pass
if __name__ == "__main__":
    main(10)