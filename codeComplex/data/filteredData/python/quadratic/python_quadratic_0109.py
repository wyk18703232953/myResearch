import random
import string

def check(map1, map2, n):
    # original three orientation checks, now parameterized
    f = True
    for i in range(n):
        for j in range(n):
            if map1[i][j] != map2[i][j]:
                f = False
                break
        if not f:
            break
    if f:
        return True

    f = True
    for i in range(n):
        for j in range(n):
            if map1[i][j] != map2[n - 1 - i][j]:
                f = False
                break
        if not f:
            break
    if f:
        return True

    f = True
    for i in range(n):
        for j in range(n):
            if map1[i][j] != map2[i][n - 1 - j]:
                f = False
                break
        if not f:
            break
    if f:
        return True

    return False


def rotate(map1, n):
    # rotate map1 90 degrees clockwise in-place
    wk1 = []
    for i in range(n):
        wk1.append([])
        for j in range(n):
            wk1[i].append(map1[i][j])

    for i in range(n):
        for j in range(n):
            map1[i][j] = wk1[n - 1 - j][i]


def generate_random_map(n):
    # generate an n x n map of random '.' or '#'
    chars = ['.', '#']
    result = []
    for _ in range(n):
        row = [random.choice(chars) for _ in range(n)]
        result.append(row)
    return result


def main(n):
    # generate test data
    map1 = generate_random_map(n)

    # decide randomly whether to make map2 a rotated/mirrored version of map1
    make_matching = random.choice([True, False])

    if make_matching:
        # choose a random transformation of map1 that check() can recognize
        map2 = []
        choice = random.randint(0, 2)
        if choice == 0:
            # identity
            for i in range(n):
                map2.append(list(map1[i]))
        elif choice == 1:
            # vertical flip of map1 -> map2[i][j] = map1[n-1-i][j]
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(map1[n - 1 - i][j])
                map2.append(row)
        else:
            # horizontal flip of map1 -> map2[i][j] = map1[i][n-1-j]
            for i in range(n):
                row = []
                for j in range(n):
                    row.append(map1[i][n - 1 - j])
                map2.append(row)
    else:
        # completely independent random map
        map2 = generate_random_map(n)

    f = False
    for _ in range(4):
        if check(map1, map2, n):
            f = True
            break
        rotate(map1, n)

    if f:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main(5)