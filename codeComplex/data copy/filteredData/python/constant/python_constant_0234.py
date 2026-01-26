def main(n):
    # n controls the size of generated "input" values deterministically
    # Generate yellow, blue, x, y, z based on n
    yellow = n
    blue = n // 2 + 1
    x = n % 7 + 1
    y = (n * 2) % 10 + 1
    z = (n * 3) % 5 + 1

    answer1 = x * 2 + y - yellow
    answer2 = z * 3 + y - blue
    if answer1 > 0:
        if answer2 > 0:
            # print(answer1 + answer2)
            pass

        else:
            # print(answer1)
            pass

    else:
        if answer2 > 0:
            # print(answer2)
            pass

        else:
            # print(0)
            pass
if __name__ == "__main__":
    main(10)