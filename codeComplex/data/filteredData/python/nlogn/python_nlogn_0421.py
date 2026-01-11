import math
import collections
import bisect

def main(n):
    # Generate deterministic input
    # Original input structure:
    #   n: length of array
    #   arr: list of n integers
    # Here we generate arr deterministically based on n
    arr = [(i * 3 + 7) % (2 * n + 1) for i in range(n)]

    counter = collections.Counter(arr)
    ans = set()
    for i in counter:
        for j in range(1, 32):
            no = 2 ** j
            diff = no - i
            if diff < 0:
                continue
            if diff == i:
                if counter[i] > 1:
                    ans.add(i)
                    break

            else:
                if diff not in counter:
                    continue

                else:
                    ans.add(i)
                    break
    val = 0
    ans = list(ans)
    for i in ans:
        val += counter[i]
    # print(n - val)
    pass
if __name__ == "__main__":
    main(10000)