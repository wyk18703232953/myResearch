def main(n):
    # Generate a deterministic string of '+' and '-' of length n
    # Example pattern: '+' if i is even, '-' if i is odd
    s = ''.join('+' if i % 2 == 0 else '-' for i in range(n))

    cur = 0
    for a in s:
        cur = max(cur, 0)
        if a == '-':
            cur -= 1

        else:
            cur += 1
        cur = max(cur, 0)
    # print(cur)
    pass
if __name__ == "__main__":
    main(10)