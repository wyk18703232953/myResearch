def main(n):
    N = n
    re = 0
    for i in range(2, N):
        t = N // i - 1
        re += t * i
    # print(re * 4)
    pass
if __name__ == "__main__":
    main(10)