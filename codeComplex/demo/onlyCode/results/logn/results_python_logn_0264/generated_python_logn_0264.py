def main(n):
    x = n
    k = n
    mod = 10 ** 9 + 7
    return 0 if x == 0 else (x * pow(2, k + 1, mod) - pow(2, k, mod) + 1 + mod) % mod

if __name__ == "__main__":
    print(main(10))