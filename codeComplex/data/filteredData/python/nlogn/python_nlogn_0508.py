def main(n):
    # Interpret n as number of pairs
    # b[0] = number of elements, b[1] = limit
    b0 = n
    # Make b1 scale roughly with n so behavior changes with n
    # For determinism and scalability, choose a simple function
    b1 = n * (n // 2 + 1)
    b = [b0, b1]

    # Deterministically generate inputs: list of [original, compressed] pairs
    # Ensure original >= compressed so that diff is non-negative
    inputs = []
    for i in range(1, b0 + 1):
        original = i * 3
        compressed = i * 2
        inputs.append([original, compressed])

    inputs_list = inputs
    diff = []
    sinComprimir = 0

    comprimido = 0
    for k in range(len(inputs_list)):
        sinComprimir = sinComprimir + inputs_list[k][0]
        diff.append(inputs_list[k][0] - inputs_list[k][1])
        comprimido = comprimido + inputs_list[k][1]

    difference = sorted(diff)
    invDifference = difference[::-1]
    newTotal = sinComprimir
    iteraciones = 0
    iterador = 0

    if sinComprimir <= b[1]:
        # print("0")
        pass
    elif comprimido > b[1]:
        # print("-1")
        pass

    else:
        while newTotal > b[1] and iterador < len(invDifference):
            iterador = iterador + 1
            newTotal = newTotal - invDifference[iterador - 1]
            iteraciones += 1
        # print(iteraciones)
        pass
if __name__ == "__main__":
    main(10)