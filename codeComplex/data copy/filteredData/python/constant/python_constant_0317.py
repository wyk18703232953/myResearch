def even_sum(arr):
    temp_sum = 0
    for each in arr:
        if each % 2 == 0:
            temp_sum += each
    return temp_sum


def main(n):
    size = 14
    stones = [(i + 1) * (n % 10 + 1) for i in range(size)]

    initial_sum = even_sum(stones)

    for i in range(size):
        duplicate = list(stones)
        temp = stones[i]
        duplicate[i] = 0
        j = i

        base_add = temp // size
        for each in range(size):
            duplicate[each] += base_add
        temp = temp % size

        while temp > 0:
            if j == size - 1:
                j = -1
            j += 1
            duplicate[j] += 1
            temp -= 1

        ts = even_sum(duplicate)
        if ts > initial_sum:
            initial_sum = ts

    # print(initial_sum)
    pass
if __name__ == "__main__":
    main(1000)