mod = 1000000007

def main(n):
    x = n
    k = n
    if x == 0:
        return 0
    else:
        return int((pow(2, k+1, mod) * x - pow(2, k, mod) + 1) % mod)

if __name__ == "__main__":
    print(main(10))