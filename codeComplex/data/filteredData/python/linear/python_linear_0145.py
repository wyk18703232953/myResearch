def main(n):
    Ab = [i % 7 for i in range(n)]
    Un = []
    Al = [0]
    r = 0
    for i in range(n):
        Al.append(max(Ab[i] + 1, Al[i]))
    for i in range(n, -1, -1):
        if Al[i - 1] < Al[i] - 1:
            Al[i - 1] = Al[i] - 1
    for i in range(n):
        Un.append(Al[i + 1] - Ab[i] - 1)
        r += Un[-1]
    return r


if __name__ == "__main__":
    # print(main(10))
    pass