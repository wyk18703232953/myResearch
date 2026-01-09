def main(n):
    # Deterministically generate input data of size n
    # Example: a is a list where each value i appears exactly twice
    a = []
    for i in range(n):
        a.append(i)
        a.append(i)
    # Core algorithm logic from original code
    ans = 0
    pos = 2 * n - 2
    for _ in range(n):
        x = a[-1]
        a.pop(-1)
        y = a.index(x)
        ans += pos - y
        pos -= 2
        a.pop(y)
    # print(ans)
    pass
if __name__ == "__main__":
    main(5)