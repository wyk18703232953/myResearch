def main(n):
    import math
    mod = 10**9 + 7
    x = n
    k = n
    return (pow(2, k+1, mod) * x - pow(2, k, mod) + 1) % mod if x > 0 else 0

if __name__ == "__main__":
    print(main(10))