def main(n):
    # Deterministically generate input of size n
    # Original program:
    # n: integer
    # nots: list of n integers
    # Here we construct nots with simple deterministic pattern using n
    if n <= 0:
        n = 1
    nots = [(i % 7) - 3 for i in range(n)]

    from math import fabs

    ampl = 0
    possible = True
    zer = False
    f_s = True
    mp = [0]

    for i in range(len(nots) - 1):
        if nots[i] == nots[i + 1]:
            if ampl != 0:
                mp.append(ampl)
                if ampl <= -5 or ampl >= 5:
                    possible = False
            mp.append(0)
            zer = True
            ampl = 0

        else:
            if nots[i] < nots[i + 1]:
                if ampl < 0 and f_s != True:
                    mp.append(ampl)
                    if ampl == -5:
                        possible = False
                    ampl = 1

                else:
                    ampl += 1

            else:
                if ampl > 0 and f_s != True:
                    mp.append(ampl)
                    if ampl == 5:
                        possible = False
                    ampl = -1

                else:
                    ampl += -1
        f_s = False

    if ampl != 0:
        mp.append(ampl)
        if ampl == -5 or ampl == 5:
            possible = False
    if len(nots) == 1:
        mp.append(0)
    mp.append(0)

    if possible:
        if zer:
            l = len(mp)
            for i in range(1, l - 1):
                if mp[i] == 0:
                    if mp[i - 1] == 4:
                        mp[i] = -1
                    if mp[i - 1] == -4:
                        mp[i] = 1
                    if mp[i + 1] == 4:
                        mp[i] = -1
                    if mp[i + 1] == -4:
                        mp[i] = 1

            for i in range(1, l - 1):
                if mp[i] == 0:
                    if mp[i - 1] >= 0 and mp[i + 1] >= 0:
                        mp[i] = -1
                    if mp[i - 1] > 0 and mp[i + 1] < 0:
                        mp[i] = 1
                    if mp[i - 1] < 0 and mp[i + 1] > 0:
                        mp[i] = -1
                    if mp[i - 1] <= 0 and mp[i + 1] <= 0:
                        mp[i] = 1

            fin = []
            ampl = mp[1]
            for i in range(1, l - 1):
                if mp[i] * mp[i + 1] > 0:
                    ampl += mp[i + 1]
                if mp[i] * mp[i + 1] < 0:
                    fin.append(ampl)
                    if ampl >= 5 or ampl <= -5:
                        possible = False
                    ampl = mp[i + 1]
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
            try:
                mp[-2] = int(fabs(mp[-2]) / mp[-2] * (fabs(mp[-2]) + 1))
            except ZeroDivisionError:
                appl = [1]
            for i in range(len(mp)):
                if mp[i] > 0:
                    for j in range(1, mp[i] + 1):
                        appl.append(j)
                if mp[i] < 0:
                    for j in range(5, 5 + mp[i], -1):
                        appl.append(j)

        if possible:
            for finger in appl:
                # print(finger, end=' ')
                pass
            # print()
            pass

        else:
            # print(-1)
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(1000)