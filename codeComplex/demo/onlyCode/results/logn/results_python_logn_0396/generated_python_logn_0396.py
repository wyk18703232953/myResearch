def main(n):
    if n == 3:
        return '1 1 3'
    done = 0
    arr = []
    for i in range(30, -1, -1):
        arr.extend([2**i] * (n // (2**i) - done))
        done += n // (2**i) - done
        if done == 1:
            k = i
    arr[0] = max(arr[0], (n // 2**(k - 1)) * 2**(k - 1))
    arr.reverse()
    return ' '.join(map(str, arr))


if __name__ == "__main__":
    print(main(10))