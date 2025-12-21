def main(n):
    M = 10 ** 9 + 7
    x = n
    k = n
    if x == 0:
        return 0
    P = pow(2, k, M)
    r = (P * x) % M - (0.5 * (-1 + P)) % M
    return int((2 * r + M) % M)

if __name__ == "__main__":
    print(main(10))