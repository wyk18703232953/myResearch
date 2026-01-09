def main(n):
    r = 0
    t = 1
    for _ in range(n - 1):
        r += t * 2
        t += 2
    # print(r + t)
    pass
if __name__ == "__main__":
    main(10)