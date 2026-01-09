def main(n):
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))
    b = 0
    for i in s:
        if i == '+':
            b += 1

        else:
            b -= 1
            b = max(b, 0)
    # print(b)
    pass
if __name__ == "__main__":
    main(10)