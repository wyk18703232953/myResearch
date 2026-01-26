import math

def main(n):
    # Generate deterministic send and rcv strings based on n
    # Pattern: first n chars from a repeating "+-" pattern for send
    # rcv is same pattern shifted by 1 position
    base = "+-"
    send = "".join(base[i % 2] for i in range(n))
    rcv = "".join(base[(i + 1) % 2] for i in range(n))

    d = {}
    d['+'] = 0
    d['-'] = 0
    for i in range(len(send)):
        d[send[i]] = d[send[i]] + 1

    flag = 1
    for i in range(len(rcv)):
        if rcv[i] in d:
            if d[rcv[i]] == 0:
                flag = 0
            else:
                d[rcv[i]] = d[rcv[i]] - 1

    tot = d['+'] + d['-']
    totComb = 2 ** tot
    n_val = tot
    r = d['+']
    if r > n_val:
        reqComb = 0
    else:
        npr = math.factorial(n_val) / math.factorial(n_val - r)
        reqComb = npr / math.factorial(r)

    if flag == 0:
        print('0.00000000')
    else:
        print(float(reqComb) / totComb)


if __name__ == "__main__":
    main(10)