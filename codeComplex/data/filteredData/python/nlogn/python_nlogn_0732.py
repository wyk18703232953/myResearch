def iskoutsu(arr):
    return len(set(arr)) == 1

def isshuntsu(arr):
    nos = [int(ele[0]) for ele in arr]
    nos.sort()
    return nos[0] + 1 == nos[1] and nos[1] + 1 == nos[2] and len(set([ele[1] for ele in arr])) == 1

def core_logic(arr):
    if isshuntsu(arr) or iskoutsu(arr):
        return 0

    total1 = 0
    if len(set(arr)) == 3:
        total1 = 2
    elif len(set(arr)) == 2:
        total1 = 1

    total2 = 2
    for ele in arr:
        no, suite = int(ele[0]), ele[1]

        if no + 2 <= 9:
            required = [str(no + 1) + suite, str(no + 2) + suite]
            curr = int(required[0] not in arr) + int(required[1] not in arr)
            total2 = min(total2, curr)

        if no + 1 <= 9 and no - 1 >= 0:
            required = [str(no - 1) + suite, str(no + 1) + suite]
            curr = int(required[0] not in arr) + int(required[1] not in arr)
            total2 = min(total2, curr)

        if no + 2 <= 9:
            required = [str(no - 1) + suite, str(no - 2) + suite]
            curr = int(required[0] not in arr) + int(required[1] not in arr)
            total2 = min(total2, curr)

    return min(total1, total2)

def generate_arr(n):
    suites = ['m', 'p', 's']
    arr = []
    for i in range(3):
        no = (n + i) % 9  # 0..8
        suite = suites[(n + i) % 3]
        arr.append(str(no) + suite)
    return arr

def main(n):
    arr = generate_arr(n)
    result = core_logic(arr)
    print(result)

if __name__ == "__main__":
    main(10)