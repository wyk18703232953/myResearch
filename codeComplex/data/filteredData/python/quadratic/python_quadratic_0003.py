import math as m

def main(n):
    if n <= 0:
        return
    r = 1
    nDiscs = n
    x = [i * 2 for i in range(nDiscs)]
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
        # print(y[i], end=' ')
        pass
    # print()
    pass
if __name__ == "__main__":
    main(10)