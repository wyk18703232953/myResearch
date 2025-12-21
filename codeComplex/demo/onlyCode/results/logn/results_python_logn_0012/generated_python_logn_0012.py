def main(n):
    l = n
    r = 2 * n
    x = 64
    while x >= 0 and (l & (1 << x)) == (r & (1 << x)):
        x -= 1
    return (1 << (x + 1)) - 1

if __name__ == "__main__":
    print(main(10))