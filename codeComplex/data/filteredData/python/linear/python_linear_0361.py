def solve(arr):
    d, s, ans = {0}, 0, 0
    for i in arr:
        s += i
        s %= 3
        if s in d:
            ans += 1
            s = 0
            d = {0}
        d.add(s)
    return ans

def main(n):
    # n is the length of the input digit string
    # generate a deterministic digit list from 1..n mapped to 0..9
    digits = [i % 10 for i in range(1, n + 1)]
    result = solve(digits)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)