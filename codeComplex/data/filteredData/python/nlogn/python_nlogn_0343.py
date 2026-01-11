def main(n):
    arr = []
    base = "abc"
    for i in range(n):
        arr.append(base * (i + 1))
    arr = sorted(arr, key=lambda x: len(x))
    for i in range(n - 1):
        if arr[i] not in arr[i + 1]:
            # print('NO')
            pass
            return
    # print('YES')
    pass
    for pal in arr:
        # print(pal)
        pass
if __name__ == "__main__":
    main(5)