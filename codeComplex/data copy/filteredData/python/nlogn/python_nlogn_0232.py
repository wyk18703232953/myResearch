def nod(a, b):
    while ((a != 0) and (b != 0)):
        if (a > b):
            a = a % b

        else:
            b = b % a
    return a + b

def point3(x1, y1, x2, y2, x3, y3):
    dy12 = x2 - x1
    dx12 = -(y2 - y1)
    dx13 = x3 - x1
    dy13 = y3 - y1
    if ((dx12 * dx13 + dy12 * dy13) == 0):
        return True

    else:
        return False

def generate_points(n):
    pts = []
    for i in range(n):
        x = i
        y = (i * 2 + 1) % (n + 3)
        pts.append([x, y])
    return pts

def main(n):
    if n < 1:
        return
    points = generate_points(n)
    lstline = []
    if (n <= 4):
        # print('YES')
        pass

    else:
        lst5 = []
        for j in range(5):
            mas = points[j]
            lst5 = lst5 + [[mas[0], mas[1]]]
        ok = True
        for i in range(3):
            for j in range(i + 1, 4, 1):
                for k in range(j + 1, 5, 1):
                    if (ok):    
                        if (point3(lst5[i][0], lst5[i][1], lst5[j][0], lst5[j][1], lst5[k][0], lst5[k][1])):
                            l1x1 = lst5[i][0]
                            l1y1 = lst5[i][1]
                            l1x2 = lst5[j][0]
                            l1y2 = lst5[j][1]
                            ok = False
        if (ok == False):
            lstline = []
            for j in range(5):
                if not(point3(l1x1, l1y1, l1x2, l1y2, lst5[j][0], lst5[j][1])):
                    lstline = lstline + [[lst5[j][0], lst5[j][1]]]
        if (ok):
            # print('NO')
            pass

        else:
            res = 'YES'
            ok1 = True
            for j in range(n - 5):
                mas = points[5 + j]
                okey1 = point3(l1x1, l1y1, l1x2, l1y2, mas[0], mas[1])
                if (ok1):
                    if (len(lstline) == 2):
                        l2x1 = lstline[0][0]
                        l2y1 = lstline[0][1]
                        l2x2 = lstline[1][0]
                        l2y2 = lstline[1][1]
                        ok1 = False
                        okey2 = point3(l2x1, l2y1, l2x2, l2y2, mas[0], mas[1])
                        if (not(okey1) and not(okey2)):
                            res = 'NO'
                    elif(not(okey1)):
                        lstline = lstline + [[mas[0], mas[1]]]
                elif(not(okey1)):
                    okey2 = point3(l2x1, l2y1, l2x2, l2y2, mas[0], mas[1])
                    if (not(okey2)):
                        res = 'NO'
            # print(res)
            pass
if __name__ == "__main__":
    main(10)