import math

def main(n):
    mod = 10**9 + 7
    x = n
    k = n
    result = (pow(2, k + 1, mod) * x - pow(2, k, mod) + 1) % mod if x > 0 else 0
    # print(result)
    pass
if __name__ == "__main__":
    main(10)