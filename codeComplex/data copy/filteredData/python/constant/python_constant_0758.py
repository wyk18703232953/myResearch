import time

def main(n):
    k = n // 2
    start = time.time()
    result = (2 * n + 3 - int((9 + 8 * (n + k)) ** 0.5)) // 2
    finish = time.time()
    # print(result)
    pass
    # elapsed = finish - start

if __name__ == "__main__":
    main(10)