def main(n):
    lst = [(i + 1) * 2 if i % 2 == 0 else (i + 1) * 2 - 1 for i in range(n)]
    evens = []
    odds = []
    for e, x in enumerate(lst):
        if x % 2 == 0:
            evens.append(e + 1)
        else:
            odds.append(e + 1)
    if len(evens) < len(odds):
        return evens[0]
    else:
        return odds[0]

if __name__ == "__main__":
    print(main(5))