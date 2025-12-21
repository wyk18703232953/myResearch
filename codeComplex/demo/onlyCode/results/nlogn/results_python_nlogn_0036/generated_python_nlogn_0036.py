def replace(arr):
    if arr == [1] * len(arr):
        arr[-1] = 2
        print(*sorted(arr))
        return ""
    arr[arr.index(max(arr))] = 1
    print(*sorted(arr))
    return ""

def main(n):
    a = n
    lst = [2] * n
    return replace(lst)

if __name__ == "__main__":
    main(5)