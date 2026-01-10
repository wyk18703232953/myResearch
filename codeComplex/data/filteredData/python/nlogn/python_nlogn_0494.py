def main(n):
    # Interpret n as number of (a,b) pairs; m and pairs are deterministically generated
    # Generate m as sum of first n integers (deterministic and scalable)
    a_values = [i + 1 for i in range(n)]
    b_values = [i // 2 for i in range(n)]
    o = 0
    c = 0
    diff = []
    for i in range(n):
        a = a_values[i]
        b = b_values[i]
        diff.append(a - b)
        o += a
        c += b
    # Define m in a deterministic way depending on n and sums
    # To exercise all branches, choose m between c and o when possible
    if o == 0:
        m = 0
    else:
        # Ensure deterministic choice: close to middle between c and o
        m = (c + o) // 2

    if m >= o:
        result = 0
    elif m < c:
        result = -1
    else:
        diff.sort(reverse=True)
        nd = o - m
        result = None
        for i in range(len(diff)):
            nd -= diff[i]
            if nd <= 0:
                result = i + 1
                break
        if result is None:
            # In case nd never <= 0, mimic no-output behavior; here we choose -1 deterministically
            result = -1
    print(result)


if __name__ == "__main__":
    # Example call with a chosen n for experimentation
    main(10)