def main(n):
    # Generate deterministic input data of size n
    a = [(i & 1) for i in range(n)]
    v = [a[0]] if n > 0 else []
    for i in range(1, n):
        if v and v[-1] == a[i]:
            v.pop()

        else:
            v.append(a[i])
    result = "NO" if len(v) > 1 else "YES"
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)