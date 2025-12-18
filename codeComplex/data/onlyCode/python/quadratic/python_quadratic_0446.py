from math import fabs
n = int(input())
nots = [int(s) for s in input().split()]
map = [0]
ampl = 0
possible = True
zer = False
f_s = True

for i in range(len(nots) - 1):                      #map
    if nots[i] == nots[i + 1]:
        if ampl != 0:
            map.append(ampl)
            if ampl <= -5 or ampl >= 5: possible = False
        map.append(0)
        zer = True
        ampl = 0
    else:
        if nots[i] < nots[i + 1]:
            if ampl < 0 and f_s != True:
                map.append(ampl)
                if ampl == -5: possible = False
                ampl = 1
            else:
                ampl += 1
        else:
            if ampl > 0 and f_s != True:
                map.append(ampl)
                if ampl == 5: possible = False
                ampl = -1
            else:
                ampl += -1
    f_s = False
if ampl != 0:
    map.append(ampl)
    if ampl == -5 or ampl == 5: possible = False
if len(nots) == 1:
    map.append(0)
map.append(0)

#print(map)

if possible == True:
    if zer == True:
        l = len(map)
        for i in range(1, l - 1):                                       #first step: 4
            if map[i] == 0:
                if map[i - 1] == 4: map[i] = -1
                if map[i - 1] == -4: map[i] = 1
                if map[i + 1] == 4: map[i] = -1
                if map[i + 1] == -4: map[i] = 1

        for i in range(1, l-1):                                        #second: > <
            if map[i] == 0:
                if map[i - 1] >= 0 and map[i + 1] >= 0: map[i] = -1
                if map[i - 1] > 0 and map[i + 1] < 0: map[i] = 1
                if map[i - 1] < 0 and map[i + 1] > 0: map[i] = -1
                if map[i - 1] <= 0 and map[i + 1] <= 0: map[i] = 1

        #print(map)

        fin = []                                                        # third: combining
        ampl = map[1]
        for i in range(1, l - 1):
            if map[i] * map[i + 1] > 0:
                ampl += map[i + 1]
            if map[i] * map[i + 1] < 0:
                fin.append(ampl)
                if ampl >= 5 or ampl <= -5: possible = False
                ampl = map[i + 1]
        fin.append(ampl)

        if possible == True:
            fin[-1] = int(fabs( fin[-1] ) / fin[-1] * (fabs( fin[-1] ) + 1))
            appl = []                                                           # forth: application
            for i in range( len(fin) ):
                if fin[i] > 0:
                    for j in range(1, fin[i] + 1):
                        appl.append(j)
                if fin[i] < 0:
                    for j in range(5, 5 + fin[i], -1):
                        appl.append(j)
        #print(fin)
        #print("*")

    else:
        appl = []
        try:
            map[-2] = int(fabs(map[-2]) / map[-2] * (fabs(map[-2]) + 1))
        except ZeroDivisionError:
            appl = [1]                                          # forth: applicature
        for i in range(len(map)):
            if map[i] > 0:
                for j in range(1, map[i] + 1):
                    appl.append(j)
            if map[i] < 0:
                for j in range(5, 5 + map[i], -1):
                    appl.append(j)
        #print("#")

    for finger in appl:
        print(finger, end = ' ')
if possible == False:
    print(-1)












