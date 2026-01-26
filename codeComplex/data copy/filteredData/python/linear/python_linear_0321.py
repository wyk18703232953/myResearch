def main(n):
    # Generate two deterministic lists of size labels based on n
    sizes = ["M", "S", "XS", "XXS", "XXXS", "L", "XL", "XXL", "XXXL"]
    k = len(sizes)
    a = [sizes[i % k] for i in range(n)]
    b = [sizes[(i * 2) % k] for i in range(n)]

    cost = 0
    for s in ["M", "S", "XS", "XXS", "XXXS", "L", "XL", "XXL", "XXXL"]:
        ca = a.count(s)
        cb = b.count(s)
        cost += ca - min(ca, cb)

    # print(cost)
    pass
if __name__ == "__main__":
    main(10)