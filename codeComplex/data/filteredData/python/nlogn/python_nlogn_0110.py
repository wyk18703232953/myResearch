def main(n):
    # n 表示列表长度
    values = [((i * 3 + 1) % (n + 5)) for i in range(n)]
    wrong = 0
    sorted_values = list(sorted(values))
    for i in range(n):
        if values[i] != sorted_values[i]:
            wrong += 1
    if wrong > 2:
        # print("NO")
        pass

    else:
        # print("YES")
        pass
if __name__ == "__main__":
    main(10)