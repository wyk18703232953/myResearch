def main(n):
    # n: number of houses; t is fixed as a deterministic constant
    t = 2
    cont = []
    for i in range(n):
        # deterministic generation of house_center and house_len
        house_center = i * 3 - n  # can be negative and spreads with n
        house_len = (i % 5) + 1   # lengths in [1,5]
        cont.append([house_center - house_len / 2, house_center + house_len / 2])

    ans = 2
    cont.sort(key=lambda element: element[0])

    for i in range(0, n - 1):
        gap = cont[i + 1][0] - cont[i][1]
        if gap > t:
            ans += 2
        elif gap == t:
            ans += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(5)