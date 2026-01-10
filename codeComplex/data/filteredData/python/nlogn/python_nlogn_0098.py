def main(n):
    # n 表示 complexity 列表的长度
    if n < 2:
        return 0

    chores = [0, 0, 1]
    complexity = [i * 2 for i in range(n)]
    complexity.sort()
    result = complexity[chores[2]] - complexity[chores[2] - 1]
    print(result)
    return result

if __name__ == "__main__":
    main(10)