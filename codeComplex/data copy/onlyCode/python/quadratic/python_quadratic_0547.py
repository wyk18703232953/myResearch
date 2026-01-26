def main():
    n = int(input())
    s = input()
    for i in range(n+1):
        flag = True
        stones = i
        for j in s:
            if j == '-':
                if stones > 0:
                    stones -= 1
                else:
                    flag = False
                    break
            else:
                stones += 1

        if flag:
            n = i
            break

    stones = n
    for i in s:
        if i == '-':
            stones -= 1
        else:
            stones += 1

    print(stones)

    

main()
