def main(n):
    kol = n
    dic = {
        'purple': 'Power',
        'green': 'Time',
        'blue': 'Space',
        'orange': 'Soul',
        'red': 'Reality',
        'yellow': 'Mind'
    }

    colors = list(dic.keys())
    r = []
    # deterministically pick the first kol colors
    for i in range(kol):
        r.append(colors[i % len(colors)])

    missing = 6 - kol if kol <= 6 else 0

    g = []
    for key in dic:
        if r.count(key) == 0:
            g.append(dic[key])

    # print(missing)
    pass
    for stone in g:
        # print(stone)
        pass
if __name__ == "__main__":
    # example call; adjust n as needed for experiments
    main(3)