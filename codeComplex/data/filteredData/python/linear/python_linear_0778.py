import math

def func(a, k):
    if a % k != 0:
        mod = 1

    else:
        mod = 0
    return math.floor(a / k) * k + mod * k

def main(n):
    # n controls the length of the list
    # deterministically generate n, m, k and the list of integers
    # Here m is unused in the logic, but kept for structural similarity
    m = n
    k = max(1, n // 3 + 1)

    arr = [(i * 2 + 3) % (5 * k) + 1 for i in range(n)]

    temp = func(int(arr[0]), k)
    c = 0
    answer = 0
    check = 'false'
    used = 0

    for i in range(len(arr)):
        arr[i] = int(arr[i])
        used = 0
        if arr[i] <= temp:
            c += 1
            check = 'true'
            used = 1
        if arr[i] >= temp:
            if check is 'true':
                answer += 1
                check = 'false'
                temp += c
                c = 0
                if arr[i] - c <= temp and used == 0:
                    c += 1
                    check = 'true'
                    used = 1

                else:
                    temp = temp + func(int(arr[i]) - temp, k)
                    if arr[i] - c <= temp and used == 0:
                        c += 1
                        check = 'true'
                        used = 1
            elif check is 'false':
                temp = temp + func(int(arr[i]) - temp, k)
                if arr[i] - c <= temp and used == 0:
                    c += 1
                    check = 'true'
                    used = 1

    result = answer if check is 'false' else answer + 1
    # print(result)
    pass
if __name__ == "__main__":
    main(1000)