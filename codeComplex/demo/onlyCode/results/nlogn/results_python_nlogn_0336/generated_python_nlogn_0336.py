def main(n):
    ar = []
    for i in range(n):
        ar.append('a' * (i + 1))
    sortedAr = sorted(ar, key=len)
    flag = False
    for i in range(n - 1):
        if sortedAr[i + 1].find(sortedAr[i]) == -1:
            flag = True
            break
    if not flag:
        return ["YES"] + sortedAr
    else:
        return ["NO"]

if __name__ == "__main__":
    result = main(5)
    for line in result:
        print(line)