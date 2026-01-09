import math

def main(n: int):
    m = 0
    limit = min(100, n)
    for i in range(limit):
        for ii in range(limit):
            for iii in range(limit):
                i1 = n - i
                ii1 = n - ii
                iii1 = n - iii
                r1 = (i1 * ii1) // math.gcd(i1, ii1)
                r2 = (r1 * iii1) // math.gcd(iii1, r1)
                if r2 > m:
                    m = r2
    # print(m)
    pass
if __name__ == "__main__":
    main(1000)