import math

def C1(n):
    # Deterministically generate input:
    # r is a fixed small integer, x_cord is a list of n integers.
    r = 1
    x_cord = [i for i in range(n)]

    y_cord = []
    for i, x in enumerate(x_cord):
        if len(y_cord) == 0:
            y_cord.append(r)

        else:
            y_cord.append(r)
            for j in range(i):
                diff = abs(x_cord[i] - x_cord[j])
                if diff <= 2 * r:
                    y_cord[i] = max(
                        y_cord[i],
                        math.sqrt(4 * r * r - diff ** 2) + y_cord[j]
                    )
    return y_cord

def main(n):
    result = C1(n)
    for v in result:
        # print(v, end=" ")
        pass
if __name__ == "__main__":
    main(10)