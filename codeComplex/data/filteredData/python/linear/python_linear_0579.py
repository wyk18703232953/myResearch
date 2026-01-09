def main(n):
    s = 2 * n + 1
    res = 0
    for i in range(n, 0, -1):
        res += s // i
        s = s % i
    return res

if __name__ == "__main__":
    # print(main(10))
    pass