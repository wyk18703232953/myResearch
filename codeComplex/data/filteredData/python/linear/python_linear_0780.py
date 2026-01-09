def main(n):
    # Deterministic data generation:
    # Create a list a of length n with a simple pattern
    # Mix of unique and duplicate values to exercise logic
    a = [(i // 2) for i in range(n)]

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
    main(10)