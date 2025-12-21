def wzor(n):
    return (n * (n + 1)) / 2

def mafia(n, c):
    po = 1
    ko = n
    sr = (po + ko) // 2
    while po != ko:
        if wzor(sr) - (n - sr) >= c:
            ko = sr
        else:
            po = sr + 1
        sr = (po + ko) // 2
    return int(wzor(po) - c)

def main(n):
    c = n // 2
    return mafia(n, c)

if __name__ == "__main__":
    print(main(10))