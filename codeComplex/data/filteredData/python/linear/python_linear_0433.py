def main(n):
    r = []
    for i in range(n):
        a = i
        b = i + 1
        c = (i * 2) % (n + 1)
        d = (i * 3) // (n + 1) if n > 0 else 0
        r.append(a + b + c + d)
    if not r:
        # print(0)
        pass
        return
    thomas = r[0]
    # print(sorted(r, reverse=True).index(thomas) + 1)
    pass
if __name__ == "__main__":
    main(10)