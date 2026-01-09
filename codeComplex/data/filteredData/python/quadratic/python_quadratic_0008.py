import math

def main(n):
    # n is the number of points
    r = 10
    x = [i * 3 for i in range(n)]
    ans = []
    for i in range(n):
        t = r
        for j in range(i):
            a = abs(x[i] - x[j])
            if a <= 2 * r:
                t2 = (2 * r) ** 2
                t2 -= a ** 2
                t2 = math.sqrt(t2) + ans[j]
                t = max(t, t2)
        ans.append(t)
    for k in ans:
        # print(k)
        pass
if __name__ == "__main__":
    main(5)