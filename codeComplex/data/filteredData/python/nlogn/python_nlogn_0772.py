def main(n):
    t = n
    results = []
    for case_id in range(1, t + 1):
        size = case_id + 1
        li = [(i * case_id + 3) % (2 * size + 5) for i in range(size)]
        li.sort()
        if size >= 2:
            val = min(li[size - 2] - 1, size - 2)
        else:
            val = -1
        results.append(val)
    return results

if __name__ == "__main__":
    # example call
    out = main(5)
    for v in out:
        print(v)