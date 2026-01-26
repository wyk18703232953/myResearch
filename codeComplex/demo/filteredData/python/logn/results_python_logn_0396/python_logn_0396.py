def main(n):
    if n == 3:
        # print('1 1 3')
        pass

    else:
        done = 0
        arr = []
        for i in range(30, -1, -1):
            cnt = n // (2 ** i) - done
            if cnt > 0:
                arr.extend([2 ** i] * cnt)
                done += cnt
                if done == 1:
                    k = i
        arr[0] = max(arr[0], (n // (2 ** (k - 1))) * (2 ** (k - 1)))
        arr.reverse()
        # print(' '.join(map(str, arr)))
        pass
if __name__ == "__main__":
    main(10)