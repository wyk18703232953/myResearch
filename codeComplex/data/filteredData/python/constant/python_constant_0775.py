from math import sqrt

def main(n):
    t = n
    results = []
    for i in range(1, t + 1):
        x = i * i * 2
        if int(sqrt(x / 2)) == sqrt(x / 2) or int(sqrt(x / 4)) == sqrt(x / 4):
            results.append("YES")

        else:
            results.append("NO")
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(10)