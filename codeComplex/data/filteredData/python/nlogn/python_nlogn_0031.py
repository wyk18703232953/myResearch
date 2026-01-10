def secondorder(arr, size):
    arr.sort()
    return arr[1]

def main(n):
    size = n
    arr = [(i * 3) % (n + 5) for i in range(n)]
    unique_list = []
    for x in arr:
        if x not in unique_list:
            unique_list.append(x)
    if len(unique_list) == 1:
        print("NO")
    else:
        print(secondorder(unique_list, size))

if __name__ == "__main__":
    main(10)