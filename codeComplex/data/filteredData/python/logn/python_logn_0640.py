def main(n):
    # Interpret n as data[0]; deterministically construct data[1]
    # Ensure data[1] is not larger than the maximum possible 'sum' for determinism tests
    # Here choose data[1] as n//3 (can be 0 as well)
    if n < 0:
        n = 0
    data0 = n
    data1 = n // 3
    data = [data0, data1]

    total_sum = 0
    cont = 0
    res = 0
    con2 = 0

    for _ in range(data[0]):
        total_sum = total_sum + con2
        con2 += 1
        res = data[0] - con2

        if data[1] == 0:
            if total_sum >= res:
                cont += 1

        else:
            if total_sum > data[1]:
                if res + 1 == total_sum - data[1]:
                    cont = res + 1
                    break

    # print(cont)
    pass
if __name__ == "__main__":
    # Example deterministic call; you can change 10 to other sizes for experiments
    main(10)