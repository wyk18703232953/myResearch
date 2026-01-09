def chk(n):
    return int(n**0.5 + 0.1) ** 2 == n

def main(n):
    t = n
    for i in range(1, t + 1):
        x = i * i
        if i % 2 == 0:
            num = 2 * x

        else:
            num = 4 * x
        if num % 2 == 0 and chk(num // 2) or num % 4 == 0 and chk(num // 4):
            # print("YES")
            pass

        else:
            # print("NO")
            pass
if __name__ == "__main__":
    main(10)