def Solution(N, Q, wariors_strength, arrows):
    prefix_sum = [0]
    for strength in wariors_strength:
        prefix_sum.append(prefix_sum[-1] + strength)
    prefix_sum.pop(0)
    arrow_so_far = 0
    for arrow in arrows:
        arrow_so_far += arrow
        if arrow_so_far >= prefix_sum[-1]:
            # print(N)
            pass
            arrow_so_far = 0

        else:
            idx = binarySearch_LowerBound(prefix_sum, arrow_so_far)
            # print(N - idx)
            pass


def binarySearch_LowerBound(arr, key):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == key:
            return mid + 1
        elif arr[mid] > key:
            r = mid - 1

        else:
            l = mid + 1
    return r + 1


def main(n):
    if n < 1:
        n = 1

    N = n
    Q = n

    wariors_strength = [i % 7 + 1 for i in range(1, N + 1)]
    arrows = [(i * 3) % (N * 4 + 5) + 1 for i in range(1, Q + 1)]

    Solution(N, Q, wariors_strength, arrows)


if __name__ == "__main__":
    main(10)