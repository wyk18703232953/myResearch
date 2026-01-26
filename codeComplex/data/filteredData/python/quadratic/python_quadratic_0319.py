n, m = 0, 0
lst = []

def generate_input(size):
    global n, m, lst
    if size < 2:
        size = 2
    n = size
    m = size // 2 if size // 2 >= 1 else 1
    lst = [((i * 7) % 13) - 6 for i in range(n)]

def main(size):
    generate_input(size)
    global n, m, lst
    maxx = 0
    arr = [0] * (n + 1)
    for i in range(n):
        summ = 0
        for j in range(i, n):
            summ += lst[j]
            arr[j - i] = max(arr[j - i], summ / (j - i + 1))
    # print(max(arr[m - 1:]))
    pass
if __name__ == "__main__":
    main(10)