def prime2(n):
    cont = 0
    flag = True
    while flag:
        if n % 2 == 0:
            cont += 1
            n = n/2
        else:
            flag = False
    if n % 4 == 1:
        return [cont, "L"]
    else:
        return [cont, "R"]

def arrivo(n,start,char):
    for i in char:
        if (i == "L" or i == "R") and start % 2 == 1:
            pass
        elif (i == "U") and 2*start == n+1:
            pass
        else:
            [power, direc] = prime2(start)
            if i == "L":
                start -= 2 ** (power - 1)
            elif i == "R":
                start += 2 ** (power - 1)
            else:
                if direc == "L":
                    start += 2 ** power
                else:
                    start -= 2 ** power
    return start

if __name__ == '__main__':
    [n,q] = map(int, raw_input().rstrip().split())
    for i in range(q):
        start = int(input())
        char = raw_input()
        print(arrivo(n,start,char))