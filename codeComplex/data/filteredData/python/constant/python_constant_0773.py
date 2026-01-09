def sq(x):
    return int(x ** 0.5) ** 2 == x

def main(n):
    t = n
    for i in range(1, t + 1):
        val = i
        if (val % 2 == 0 and sq(val // 2)) or (val % 4 == 0 and sq(val // 4)):
            # print('YES')
            pass

        else:
            # print('NO')
            pass
if __name__ == "__main__":
    main(10)