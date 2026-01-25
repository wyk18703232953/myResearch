from collections import Counter

def main(n):
    # n 表示数组长度
    if n <= 0:
        return 0

    # 确定性生成 c 和数组 a
    c = 1
    a = [(i % 5) + 1 for i in range(n)]

    counter = Counter()
    minus = 0
    count = a.count(c)
    maxi = 0
    for i in range(n):
        if a[i] != c:
            if counter[a[i]] < minus:
                counter[a[i]] = minus
            counter[a[i]] += 1
            maxi = max(maxi, counter[a[i]] + count - minus)
        else:
            minus += 1
    result = max(maxi, minus)
    print(result)
    return result

if __name__ == "__main__":
    # 示例调用，可自行修改 n 的大小做实验
    main(10)