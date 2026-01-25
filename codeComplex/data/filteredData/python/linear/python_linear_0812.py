def main(n):
    # Generate a deterministic array of length n
    # Example rule: arr[i] = i % 5
    arr = [i % 5 for i in range(n)]

    dic = {}
    for val in arr:
        if val not in dic:
            dic[val] = 1
        else:
            dic[val] += 1

    flag1 = True
    if 0 in dic:
        if dic[0] >= 2:
            flag1 = False
    cnt = 0
    for val in dic.keys():
        if dic[val] >= 3:
            flag1 = False
            break
        if dic[val] == 2:
            cnt += 1
            if val - 1 in dic:
                flag1 = False
                break
    if cnt >= 2:
        flag1 = False
    if flag1 is False:
        print('cslnb')
    else:
        flag2 = (n * (n - 1) // 2 + sum(arr)) % 2
        if flag2 == 1:
            print('sjfnb')
        else:
            print('cslnb')


if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)