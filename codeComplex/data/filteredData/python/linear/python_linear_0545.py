def main(n):
    # n 表示数组长度
    a = [i // 2 for i in range(n)]
    mx = -1
    for step, elem in enumerate(a):
        if elem > mx + 1:
            print(step + 1)
            return
        else:
            mx = max(mx, elem)
    print(-1)


if __name__ == "__main__":
    main(10)