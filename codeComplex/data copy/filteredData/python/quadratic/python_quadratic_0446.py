from math import fabs

def main(n):
    if n < 1:
        n = 1

    # 构造确定性的输入 nots，长度为 n
    # 使用简单的周期模式，包含上升、下降和相等情况
    base = [0, 1, 1, 2, 1, 1, 0]
    nots = [base[i % len(base)] + (i // len(base)) for i in range(n)]

    map_vals = [0]
    ampl = 0
    possible = True
    zer = False
    f_s = True

    for i in range(len(nots) - 1):
        if nots[i] == nots[i + 1]:
            if ampl != 0:
                map_vals.append(ampl)
                if ampl <= -5 or ampl >= 5:
                    possible = False
            map_vals.append(0)
            zer = True
            ampl = 0

        else:
            if nots[i] < nots[i + 1]:
                if ampl < 0 and f_s is not True:
                    map_vals.append(ampl)
                    if ampl == -5:
                        possible = False
                    ampl = 1

                else:
                    ampl += 1

            else:
                if ampl > 0 and f_s is not True:
                    map_vals.append(ampl)
                    if ampl == 5:
                        possible = False
                    ampl = -1

                else:
                    ampl += -1
        f_s = False

    if ampl != 0:
        map_vals.append(ampl)
        if ampl == -5 or ampl == 5:
            possible = False
    if len(nots) == 1:
        map_vals.append(0)
    map_vals.append(0)

    if possible:
        if zer:
            l = len(map_vals)
            for i in range(1, l - 1):
                if map_vals[i] == 0:
                    if map_vals[i - 1] == 4:
                        map_vals[i] = -1
                    if map_vals[i - 1] == -4:
                        map_vals[i] = 1
                    if map_vals[i + 1] == 4:
                        map_vals[i] = -1
                    if map_vals[i + 1] == -4:
                        map_vals[i] = 1

            for i in range(1, l - 1):
                if map_vals[i] == 0:
                    if map_vals[i - 1] >= 0 and map_vals[i + 1] >= 0:
                        map_vals[i] = -1
                    if map_vals[i - 1] > 0 and map_vals[i + 1] < 0:
                        map_vals[i] = 1
                    if map_vals[i - 1] < 0 and map_vals[i + 1] > 0:
                        map_vals[i] = -1
                    if map_vals[i - 1] <= 0 and map_vals[i + 1] <= 0:
                        map_vals[i] = 1

            fin = []
            ampl = map_vals[1]
            for i in range(1, l - 1):
                if map_vals[i] * map_vals[i + 1] > 0:
                    ampl += map_vals[i + 1]
                if map_vals[i] * map_vals[i + 1] < 0:
                    fin.append(ampl)
                    if ampl >= 5 or ampl <= -5:
                        possible = False
                    ampl = map_vals[i + 1]
            fin.append(ampl)

            if possible:
                fin[-1] = int(fabs(fin[-1]) / fin[-1] * (fabs(fin[-1]) + 1))
                appl = []
                for i in range(len(fin)):
                    if fin[i] > 0:
                        for j in range(1, fin[i] + 1):
                            appl.append(j)
                    if fin[i] < 0:
                        for j in range(5, 5 + fin[i], -1):
                            appl.append(j)

            else:
                appl = []

        else:
            appl = []
            try:
                map_vals[-2] = int(fabs(map_vals[-2]) / map_vals[-2] * (fabs(map_vals[-2]) + 1))
            except ZeroDivisionError:
                appl = [1]
            for i in range(len(map_vals)):
                if map_vals[i] > 0:
                    for j in range(1, map_vals[i] + 1):
                        appl.append(j)
                if map_vals[i] < 0:
                    for j in range(5, 5 + map_vals[i], -1):
                        appl.append(j)

        if possible:
            for finger in appl:
                # print(finger, end=' ')
                pass

        else:
            # print(-1)
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(20)