import math

def main(n):
    k = n

    flag = True
    i = 0
    value = 0

    if k <= 9:
        # print(k)
        pass

    else:
        while flag:
            a = 9 * pow(10, i) * (i + 1)
            if k >= a:
                k -= a
                value += 9 * pow(10, i)
                i += 1

            else:
                num = int(math.ceil(k / (i + 1)))
                value += num
                index = k % (i + 1) - 1
                # print(str(value)[index])
                pass
                flag = False

if __name__ == "__main__":
    main(1000000)