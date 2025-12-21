def main(n):
    A = [9, 189, 2889, 38889, 488889, 5888889, 68888889, 788888889, 8888888889, 98888888889, 1088888888889, float('inf')]
    k = n
    if k < 10:
        return k
    else:
        for i in range(0, 12):
            if k > A[i + 1]:
                continue
            else:
                a = 10 ** (i + 1) + (k - A[i] - 1) // (i + 2)
                b = (k - A[i] - 1) % (i + 2)
                return int(str(a)[b])

if __name__ == "__main__":
    print(main(100))