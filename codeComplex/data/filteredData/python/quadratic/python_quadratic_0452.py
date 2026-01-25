def main(n):
    # Generate a deterministic permutation of 1..n based on a simple arithmetic rule
    # Example pattern: odd positions get increasing odds, even positions get increasing evens
    # Ensures it's a permutation of [1..n]
    odds = [i for i in range(1, n + 1, 2)]
    evens = [i for i in range(2, n + 1, 2)]
    arr = []
    oi = 0
    ei = 0
    for i in range(n):
        if i % 2 == 0:
            if oi < len(odds):
                arr.append(odds[oi])
                oi += 1
            else:
                arr.append(evens[ei])
                ei += 1
        else:
            if ei < len(evens):
                arr.append(evens[ei])
                ei += 1
            else:
                arr.append(odds[oi])
                oi += 1

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
        if len(dict1[arr[arr1[i]]]) == 0:
            strarr[arr1[i]] = 'B'
        else:
            if len(dict1[arr[arr1[i]]]) == 1 and len(dict1[dict1[arr[arr1[i]]][0]]) == 0:
                strarr[arr1[i]] = 'A'
            else:
                flag = 0
                for j in dict1[arr[arr1[i]]]:
                    if strarr[arr1[j - 1]] == 'B':
                        flag = 1
                        break
                if flag == 1:
                    strarr[arr1[i]] = 'A'
                else:
                    strarr[arr1[i]] = 'B'
    result = "".join(x for x in strarr)
    print(result)
    return result


if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)