import random

def need_changes(vals):
    # vals: sorted list of 1~9, length 1~3
    l = len(vals)
    if l == 3:
        # three tiles
        if vals[0] == vals[1] == vals[2]:
            return 0
        if vals[0] == vals[1] or vals[1] == vals[2]:
            return 1
        if vals[0] + 1 == vals[1] and vals[1] + 1 == vals[2]:
            return 0
        if vals[0] + 1 == vals[1] or vals[1] + 1 == vals[2]:
            return 1
        if vals[0] + 2 == vals[1] or vals[1] + 2 == vals[2]:
            return 1
        return 2
    elif l == 2:
        # two tiles
        if vals[0] == vals[1]:
            return 1
        if vals[0] + 1 == vals[1]:
            return 1
        if vals[0] + 2 == vals[1]:
            return 1
        return 2
    else:
        # 0 or 1 tile in the suit
        return 2

def main(n):
    # n is the scale; here we use it only to seed the RNG for reproducibility
    random.seed(n)

    suits = ['p', 's', 'm']
    # Generate 3 random tiles like "1p", "9s", etc.
    tiles = []
    for _ in range(3):
        v = random.randint(1, 9)
        s = random.choice(suits)
        tiles.append(f"{v}{s}")

    # Mimic original grouping logic
    s = []
    p = []
    m = []

    a, b, c = tiles
    for t in (a, b, c):
        v = int(t[0])
        suit = t[1]
        if suit == 'p':
            p.append(v)
        elif suit == 's':
            s.append(v)
        else:
            m.append(v)

    s.sort()
    p.sort()
    m.sort()

    cur = need_changes(s)
    x = need_changes(p)
    y = need_changes(m)

    print(min(cur, x, y))

if __name__ == "__main__":
    # example run with n = 1
    main(1)