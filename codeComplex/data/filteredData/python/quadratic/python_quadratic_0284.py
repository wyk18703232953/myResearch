def main(n):
    # Ensure n is at least 1 to avoid empty inputs
    if n < 1:
        n = 1

    # Deterministically generate k based on n
    k = n // 2 if n >= 2 else 1

    # Generate lst1 as n distinct integers (0 to n-1)
    lst1 = list(range(n))

    # Generate lst2 as k integers that are a deterministic permutation/pattern from lst1
    # Here we choose every second element starting from 1, wrapping around if needed
    lst2 = [lst1[(2 * i + 1) % n] for i in range(k)]

    lst3 = {}
    ans = []
    for i in lst2:
        if i in lst1:
            lst3[i] = lst1.index(i)
    for i in sorted(lst3, key=lst3.get):
        ans.append(i)
    # print(*ans, sep=" ")
    pass
if __name__ == "__main__":
    # Example call; you can change 10 to other n to scale input size
    main(10)