def main(n):
    # Deterministically generate input array 'a' of length n
    # Example pattern: a[i] = i // 2
    a = [i // 2 for i in range(n)]

    mx = -1
    for step, elem in enumerate(a):
        if elem > mx + 1:
            # print(step + 1)
            pass
            return

        else:
            mx = max(mx, elem)
    # print(-1)
    pass
if __name__ == "__main__":
    main(10)