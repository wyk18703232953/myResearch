def main(n):
    x = n
    k = n
    m = 10**9 + 7
    if x > 0:
        return (x * pow(2, k + 1, m) - pow(2, k, m) + 1) % m
    else:
        return 0

if __name__ == "__main__":
    print(main(10))