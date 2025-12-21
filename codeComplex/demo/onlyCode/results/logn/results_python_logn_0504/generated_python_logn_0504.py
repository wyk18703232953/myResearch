def main(n):
    L = [(i + 1) * 9 * 10 ** i for i in range(12)]
    number = n
    exponent = 0
    while number >= 0:
        number -= L[exponent]
        exponent += 1
        if exponent == len(L):
            break
    exponent -= 1
    number %= L[exponent]
    start = 10 ** exponent
    numDigits = exponent + 1
    final = start + (number // numDigits - 1)
    remainder = number % numDigits
    if remainder == 0:
        final = str(final)
        return final[-1]
    else:
        final = str(final + 1)
        return final[remainder - 1]

if __name__ == "__main__":
    print(main(100))