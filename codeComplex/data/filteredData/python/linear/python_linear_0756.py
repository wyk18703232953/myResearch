def main(n):
    # Generate deterministic input list of length n
    # Example pattern: alternating non-negative and negative, scaled by index
    l1 = [i if i % 3 != 0 else -i for i in range(n)]
    
    if n % 2 == 0:
        for i in range(n):
            if l1[i] >= 0:
                l1[i] = -1 * l1[i] - 1

    else:
        for i in range(n):
            if l1[i] >= 0:
                l1[i] = -1 * l1[i] - 1
        idx = l1.index(min(l1))
        l1[idx] = l1[idx] * -1 - 1

    # print(' '.join(str(x) for x in l1))
    pass
if __name__ == "__main__":
    main(10)