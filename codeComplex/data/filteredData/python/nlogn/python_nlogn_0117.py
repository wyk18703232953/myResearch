def main(n):
    # 生成确定性的数组，规模为 n
    # 例如：arr[i] = (i * 3 + 1) % (n + 5)
    arr = [(i * 3 + 1) % (n + 5) for i in range(n)]

    ab = sorted(arr)
    t = [i for i in range(n) if arr[i] != ab[i]]
    if len(t) < 3:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main(10)