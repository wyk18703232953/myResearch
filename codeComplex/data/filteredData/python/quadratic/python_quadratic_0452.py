def main(n):
    # Deterministically generate input array of size n
    # Original constraints imply arr[i] in [1, n], so we use a simple modular pattern
    if n <= 0:
        # print("")
        pass
        return

    arr = [(i % n) + 1 for i in range(n)]

    dict1 = {}
    arr1 = [0] * n
    for i in range(n):
        arr1[arr[i] - 1] = i
    for i in range(n):
        dict1[i + 1] = []
    for i in range(n):
        for j in range(i - arr[i], -1, -arr[i]):
            if arr[j] > arr[i]:
                dict1[arr[i]].append(arr[j])
        for j in range(i + arr[i], n, arr[i]):
            if arr[j] > arr[i]:
                dict1[arr[i]].append(arr[j])
    strarr = ['.'] * n
    for i in range(n - 1, -1, -1):
        cur_val = arr[arr1[i]]
        if len(dict1[cur_val]) == 0:
            strarr[arr1[i]] = 'B'

        else:
            first_neighbor = dict1[cur_val][0]
            if len(dict1[first_neighbor]) == 0:
                strarr[arr1[i]] = 'A'

            else:
                flag = 0
                for j in dict1[cur_val]:
                    if strarr[arr1[j - 1]] == 'B':
                        flag = 1
                        break
                if flag == 1:
                    strarr[arr1[i]] = 'A'

                else:
                    strarr[arr1[i]] = 'B'
    # print("".join(strarr))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for scalability experiments
    main(10)