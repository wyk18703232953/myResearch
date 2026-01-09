def main(n):
    # Interpret n as the number of elements in the array
    # Deterministically generate array: [0, 1, 2, ..., n-1]
    a = set(range(n))
    ans = len(a) - 1 if 0 in a else len(a)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)