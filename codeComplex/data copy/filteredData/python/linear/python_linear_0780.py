def main(n):
    # Generate deterministic input based on n
    # n is both the number of elements and controls their values
    # Example scheme: a[i] = i // 2 to create some predictable duplicates
    a = [i // 2 for i in range(n)]

    dupes = 0
    dupeVal = -1
    d = set()
    for el in a:
        if el in d:
            dupes += 1
            dupeVal = el

        else:
            d.add(el)

    inPlay = True
    if dupes > 1:
        # print('cslnb')
        pass
        inPlay = False
    elif dupes == 1:
        if dupeVal == 0 or (dupeVal - 1) in d:
            # print('cslnb')
            pass
            inPlay = False

    if inPlay:
        finalSum = (n * (n - 1)) // 2
        Sum = sum(a)
        if (Sum - finalSum) % 2 == 0:
            # print('cslnb')
            pass

        else:
            # print('sjfnb')
            pass
if __name__ == "__main__":
    # Example deterministic runs for different scales
    for n in [1, 2, 3, 5, 10]:
        main(n)