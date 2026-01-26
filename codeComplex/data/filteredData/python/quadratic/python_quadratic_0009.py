def main(n):
    import math

    # n: number of circles
    # deterministically generate radius and x_list
    # radius is fixed positive integer
    radii = 5

    # generate strictly increasing x coordinates with step 1
    # x_list length = n
    x_list = list(range(n))

    temp_arr = []
    for i in range(n):
        temp_arr.append(
            max(
                [radii]
                + [
                    math.sqrt(4 * radii ** 2 - (x_list[i] - x_list[j]) ** 2) + temp_arr[j]
                    for j in range(i)
                    if abs(x_list[i] - x_list[j]) <= 2 * radii
                ]
            )
        )

    for i in temp_arr:
        # print(i, end=" ")
        pass
if __name__ == "__main__":
    main(10)