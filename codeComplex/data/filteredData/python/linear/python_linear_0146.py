def main(n):
    # Deterministically generate Ab as a list of length n
    Ab = [(i * 3) % (n + 5) for i in range(n)]

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
    # Example call; adjust n as needed for experiments
    result = main(10)
    # print(result)
    pass