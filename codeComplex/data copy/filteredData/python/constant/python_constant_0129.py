def main(n):
    if n >= 0:
        # print(n)
        pass

    else:
        if ((n * -1) // 10) == 0:
            # print(0)
            pass

        else:
            n *= -1
            y = n // 10
            z = n % 10
            x = y // 10
            x *= 10
            x += z
            x *= -1
            y *= -1
            if x >= y:
                # print(x)
                pass

            else:
                # print(y)
                pass
if __name__ == "__main__":
    main(123456789)