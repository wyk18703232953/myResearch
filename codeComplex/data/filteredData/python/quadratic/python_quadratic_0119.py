import collections
import bisect

def main(n):
    m = n
    arr = [i % n + 1 for i in range(m)]
    cs = collections.Counter(arr)
    result = min(cs[x] for x in range(1, n + 1))
    # print(result)
    pass
if __name__ == "__main__":
    main(10)