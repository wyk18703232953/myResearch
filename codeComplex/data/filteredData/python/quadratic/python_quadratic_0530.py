i = 0
v = 0
g = 0
s = 0

def main(n):
    global i, v, g, s
    i = n
    v = 0
    g = 2
    s = 4
    while g <= i:
        while s <= i:
            v = v + int(s / g * 4)
            s = s + g
        g = g + 1
        s = g * 2
    print(str(v))

if __name__ == "__main__":
    main(10)