import math

def score(x):
    ans = 0
    xr = math.ceil(math.sqrt(x))

    divs = []
    for i in range(1, xr + 3):
        if x % i == 0:
            divs.append(i)
            divs.append(x // i)

    divs = sorted(list(set(divs)))

    for l in divs[1:-1]:
        ans += x // l

    return ans

def main(n):
    if n <= 3:
        # print(0)
        pass
        return

    ans = 0
    for i in range(4, n + 1):
        ans += score(i)

    # print(ans * 4)
    pass
if __name__ == "__main__":
    # 示例：以 n = 100 作为输入规模
    main(100)