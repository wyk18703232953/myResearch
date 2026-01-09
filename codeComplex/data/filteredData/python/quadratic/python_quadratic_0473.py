def main(n):
    # Generate deterministic l and r based on n
    # l[i]: number of greater elements on the left
    # r[i]: number of greater elements on the right
    l = [i % (n // 2 + 1) for i in range(n)]
    r = [(n - 1 - i) % (n // 2 + 1) for i in range(n)]

    candies = []
    for i in range(n):
        candies.append(n - l[i] - r[i])

    left = []
    for i in range(n):
        guys = 0
        for j in range(i):
            if candies[j] > candies[i]:
                guys += 1
        left.append(guys)

    right = []
    for i in range(n):
        guys = 0
        for j in range(i, n):
            if candies[j] > candies[i]:
                guys += 1
        right.append(guys)

    if left == l and right == r:
        # print("YES")
        pass
        candiesstr = ""
        for i in range(n):
            candiesstr += str(candies[i]) + " "
        # print(candiesstr[:len(candiesstr) - 1])
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)