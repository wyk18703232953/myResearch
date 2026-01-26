def main(n):
    # Interpret n as the distance between x and y; fix other parameters deterministically
    x = 0
    y = n
    z = n // 2
    t1 = 2
    t2 = 1
    t3 = 1

    lift_time = (abs(z - x) + abs(y - x)) * t2 + 3 * t3
    stairs_time = abs(y - x) * t1

    if lift_time <= stairs_time:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(100000)