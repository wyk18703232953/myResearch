n,k = map(int, raw_input().split())

def area(height):
    return n * height


def bin_search(low, high):
    if (high == low):
        return high
    if high - low == 1:
        if area(low) >= k:
            return low
        return high
    midd = (high + low) // 2
    if area(midd) > k:
        return bin_search(low, midd)
    return bin_search(midd, high)

print(bin_search(0, 1000000000000000000))