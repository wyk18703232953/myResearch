from math import ceil

def paper(a, b, c, d):
    return ceil((a * (ceil(b / c))) / d)

def main(n):
    a = n
    b = n * 2 + 1
    c = n // 2 + 1
    d = n + 3
    result = paper(a, b, c, d)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)