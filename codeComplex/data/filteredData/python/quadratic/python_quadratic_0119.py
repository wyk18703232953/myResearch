import collections
import bisect

def main(n):
    # 生成确定性的 m 和数组 arr
    # 这里令 m = n，并构造一个长度为 m 的数组
    # arr[i] = (i % n) + 1，使得 1..n 均匀出现
    if n <= 0:
        return
    m = n
    arr = [(i % n) + 1 for i in range(m)]

    cs = collections.Counter(arr)
    result = min(cs[x] for x in range(1, n + 1))
    # print(result)
    pass
if __name__ == "__main__":
    main(10)