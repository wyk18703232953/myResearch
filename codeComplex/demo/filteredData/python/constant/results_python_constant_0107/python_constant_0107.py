def operations(a, b):
    less = min(a, b)
    more = max(a, b)
    ops = 0
    while less > 0 and more > 0:
        ops += more // less
        more -= less * (more // less)
        less, more = more, less
    return ops

def main(n):
    results = []
    for i in range(1, n + 1):
        a = i
        b = 2 * i + 1
        results.append(operations(a, b))
    for res in results:
        # print(res)
        pass
if __name__ == "__main__":
    main(10)