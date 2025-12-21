m = 1000000007

def main(n):
    x = n
    k = n
    up = (x * pow(2, k + 1, m)) % m
    down = pow(2, k, m) - 1
    if x == 0:
        return 0
    else:
        return (up - down) % m

if __name__ == "__main__":
    print(main(10))