def main(n):
    l = list(range(1, n + 1))
    l = set(l)
    l = list(l)
    if len(l) <= 1:
        return "NO"
    l.sort()
    return l[1]

if __name__ == "__main__":
    print(main(5))