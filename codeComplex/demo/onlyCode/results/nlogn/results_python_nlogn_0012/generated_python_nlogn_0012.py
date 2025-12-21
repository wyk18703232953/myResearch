import random
from collections import defaultdict

def main(n):
    exist_num = n
    new_width = max(1, n // 2)
    buildings = []
    centers = sorted(random.randint(0, 10 * n + 10) for _ in range(exist_num))
    for center in centers:
        width = random.randint(1, max(1, n))
        buildings.append((center - width / 2, center + width / 2))
    buildings.sort()
    possible_loc = 2
    for left, right in zip(buildings, buildings[1:]):
        gap = right[0] - left[1]
        if gap == new_width:
            possible_loc += 1
        elif gap > new_width:
            possible_loc += 2
    print(possible_loc)

if __name__ == "__main__":
    main(10)