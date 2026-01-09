def main(n):
    lst = [(i * 2 + (i % 3)) for i in range(n)]

    evens = []
    odds = []

    for e, x in enumerate(lst):
        if x % 2 == 0:
            evens.append(e + 1)

        else:
            odds.append(e + 1)

    if len(evens) < len(odds):
        # print(evens[0] if evens else -1)
        pass

    else:
        # print(odds[0] if odds else -1)
        pass
if __name__ == "__main__":
    main(10)