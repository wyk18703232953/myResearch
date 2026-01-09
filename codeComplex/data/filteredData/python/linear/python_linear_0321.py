def main(n):
    sizes_order = ["M", "S", "XS", "XXS", "XXXS", "L", "XL", "XXL", "XXXL"]
    k = len(sizes_order)

    a = [sizes_order[i % k] for i in range(n)]
    b = [sizes_order[(i * 2 + 1) % k] for i in range(n)]

    cost = 0
    for s in sizes_order:
        ca = a.count(s)
        cb = b.count(s)
        cost += ca - min(ca, cb)
    # print(cost)
    pass
if __name__ == "__main__":
    main(1000)