from math import sqrt, floor, ceil

def main(n):
    ran = list(range(2, 1 + n // 2))
    xx = [d * (n // d - 1) for d in ran]
    print(sum(xx) * 4)

if __name__ == "__main__":
    main(1000)