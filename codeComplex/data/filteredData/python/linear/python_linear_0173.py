n = None

def main(size):
    global n
    n = size
    if n >= 6:
        for i in range(2, n - 1):
            print(1, i)
        for i in range(n - 1, n + 1):
            print(2, i)
    else:
        print(-1)
    for i in range(2, n + 1):
        print(1, i)

if __name__ == "__main__":
    main(10)