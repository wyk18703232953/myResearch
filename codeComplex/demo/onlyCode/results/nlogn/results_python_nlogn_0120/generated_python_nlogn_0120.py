def main(n):
    arr = list(range(1, n + 1))
    if n >= 2:
        arr[0], arr[1] = arr[1], arr[0]
    li = arr[:]
    li.sort()
    c = 0
    for i in range(n):
        if arr[i] != li[i]:
            c += 1
        if c > 2:
            return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    print(main(5))