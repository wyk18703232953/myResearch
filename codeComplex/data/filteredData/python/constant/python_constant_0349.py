lst = []
ans = {'purple': 'Power', 'green': 'Time', 'blue': 'Space', 'orange': 'Soul', 'red': 'Reality', 'yellow': 'Mind'}

def main(n):
    lst = []
    colors = list(ans.keys())
    k = len(colors)
    for i in range(n):
        c = colors[i % k]
        if c not in lst:
            lst.append(c)
    a = []
    for color in ans.keys():
        if color not in lst:
            a.append(ans[color])
    # print(len(a))
    pass
    for x in a:
        # print(x)
        pass
if __name__ == "__main__":
    main(3)