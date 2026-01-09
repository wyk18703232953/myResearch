import math

def main(n):
    results = []
    for _ in range(n):
        num = _ + 1
        s = 1
        ch = 0
        for i in range(1, 31):
            s *= 2
            d = math.sqrt(num // s)
            if num % s == 0 and d == int(d):
                ch = 1
                break
        if ch:
            results.append("YES")

        else:
            results.append("NO")
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)