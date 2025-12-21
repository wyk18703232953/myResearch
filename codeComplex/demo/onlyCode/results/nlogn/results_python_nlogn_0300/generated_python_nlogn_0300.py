def main(n):
    w = list(range(1, n + 1))
    intro = [[v, i] for i, v in enumerate(w, 1)]
    intro.sort(key=lambda x: x[0])
    s = ("0" * n) + ("1" * n)
    i = -1
    li = []
    ans = []
    for j in s:
        if j == "0":
            i += 1
            ans.append(intro[i][1])
            li.append(intro[i][1])
        else:
            ans.append(li.pop(-1))
    return ans

if __name__ == "__main__":
    res = main(5)
    print(" ".join(map(str, res)))