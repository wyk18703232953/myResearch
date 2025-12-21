def main(n):
    k = 2
    arr = list(range(1, n + 1))
    arr.sort()
    dic = {}
    for a in arr:
        if a / k not in dic:
            dic[a] = 1
    return len(dic)

if __name__ == "__main__":
    print(main(10))