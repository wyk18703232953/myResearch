def main(n):
    # Generate deterministic test data of size n
    # Here we use a simple arithmetic pattern based on n
    # Example: a[i] = (i * 2 + 3) % (n + 5)
    a = [(i * 2 + 3) % (n + 5) for i in range(n)]

    s = sorted(a)
    q = a.index(max(a))
    q1, q = min(len(a) - 1, q + 1), max(0, q - 1)
    for q2 in range(len(a) - 2, -1, -1):
        if a[q] == s[q2]:
            q = max(0, q - 1)
        elif a[q1] == s[q2]:
            q1 = min(len(a) - 1, q1 + 1)

        else:
            # print("NO")
            pass
            break

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(10)