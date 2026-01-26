x1, y1, x2, y2, x3, y3 = map(int, input().split())
rect1 = [x1, y1]
rect2 = [x2, y2]
rect3 = [x3, y3]
def func():
    rect11 = [x1, y1]
    rect22 = [x2, y2]
    rect33 = [x3, y3]
    rect1 = [x1, y1]
    rect2 = [x2, y2]
    rect3 = [x3, y3]

    recta = [x1, y1]
    rectb = [x2, y2]
    rectc = [x3, y3]
    for i in rect11:
        for ii in rect22:
            for iii in rect33:
                if i==ii:
                    rect1.remove(i)
                    rect2.remove(ii)
                    if rect1[0]+rect2[0]==iii:
                        rect3.remove(iii)
                        if i+rect3[0]==iii:
                            print(iii)
                            for j in range(iii):
                                if j<rect1[0]:
                                    print("C"*rect3[0]+"A"*i)
                                else:
                                    print("C"*rect3[0]+"B"*ii)
                            exit()
                rect1=recta.copy()
                rect2=rectb.copy()
                rect3=rectc.copy()

                if i==iii:
                    rect1.remove(i)
                    rect3.remove(iii)
                    if rect1[0]+rect3[0]==ii:
                        rect2.remove(ii)
                        if i+rect2[0]==ii:
                            print(ii)

                            for j in range(ii):
                                if j<rect1[0]:
                                    print("B"*rect2[0]+"A"*i)
                                else:
                                    print("B"*rect2[0]+"C"*iii)
                            exit()
                rect1 = recta.copy()
                rect2 = rectb.copy()
                rect3 = rectc.copy()
                if ii==iii:
                    rect2.remove(ii)
                    rect3.remove(iii)
                    if rect2[0]+rect3[0]==i:
                        rect1.remove(i)
                        if i==rect1[0]+ii:
                            print(i)
                            for j in range(i):
                                if j<rect2[0]:
                                    print("A"*rect1[0]+"B"*ii)
                                else:print("A"*rect1[0]+"C"*iii)
                            exit()
                rect1=recta.copy()
                rect2=rectb.copy()
                rect3=rectc.copy()
    return print(-1)
for i in rect1:
    for ii in rect2:
        for iii in rect3:
            recta = [x1, y1]
            rectb = [x2, y2]
            rectc = [x3, y3]

            if i==ii==iii:
                rect1.remove(i)
                rect2.remove(i)
                rect3.remove(i)

            if rect1[0]+rect2[0]+rect3[0]==i:
                print(i)
                for j in range(i):
                    print("A"*rect1[0]+"B"*rect2[0]+"C"*rect3[0])
                exit()
            rect1=recta
            rect2=rectb
            rect3=rectc

func()
