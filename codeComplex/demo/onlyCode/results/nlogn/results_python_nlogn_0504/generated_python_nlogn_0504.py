def main(n):
    m = n * 2 // 3
    entries = []
    for i in range(n):
        a = i + 2
        b = i % 3
        entries.append((a, b, a - b))
    from functools import reduce
    entries.sort(key=lambda x: x[2], reverse=True)
    size = reduce(lambda s, e: s + e[0], entries, 0)
    count = 0
    while size > m and count < n:
        size -= entries[count][2]
        count += 1
    return -1 if size > m else count

if __name__ == "__main__":
    print(main(10))