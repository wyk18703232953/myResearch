import math as m

def main(n):
    # n controls number of discs; radius r is fixed deterministically
    if n <= 0:
        return
    r = 1
    nDiscs = n

    # Deterministic x positions: spaced by r so many will interact (diffX <= 2r)
    x = [i for i in range(nDiscs)]
    y = []

    for i in range(len(x)):
        tempY = [r]
        for j in range(i):
            diffX = abs(x[i] - x[j])
            if diffX <= (2 * r):
                addY = m.sqrt((4 * r * r) - (diffX * diffX))
                tempY.append(y[j] + addY)
        y.append(max(tempY))

    for i in range(len(y)):
        print(y[i], end=' ')
    print()


if __name__ == "__main__":
    # Example deterministic run; change n to test other scales
    main(10)