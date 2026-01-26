"""
[input1]


[output1]


[input2]


[output2]

"""

from sys import stdin

sys_input = stdin.readline


def si(): return sys_input().rstrip()


def ii(): return int(si())


def sti(): return si().split()


def iti(): return map(int, sti())


def sli(): return list(si())


def ili(): return list(iti())


def main():
    B.sort(reverse=True)
    G.sort(reverse=True)

    if B[0] > G[-1]:
        print(-1)
        return

    boy_capacities = [M - 1] * N
    current_capable_boy_index = 0
    #sweets = [[b] * M for b in B]
    result = sum(B) * M

    for j, g in enumerate(G):
        yet = True
        while yet:
            if B[current_capable_boy_index] < g and boy_capacities[current_capable_boy_index] > 0:
                result += g - B[current_capable_boy_index]
                #sweets[current_capable_boy_index][j] = g
                boy_capacities[current_capable_boy_index] -= 1
                yet = False
            elif B[current_capable_boy_index] == g:
                result += g - B[current_capable_boy_index]
                #sweets[current_capable_boy_index][j] = g
                yet = False
            else:
                current_capable_boy_index += 1
                if current_capable_boy_index > N - 1:
                    print(-1)
                    return

    #print(sweets)
    print(result)

    return


if __name__ == '__main__':
    N, M = iti()
    B = ili()
    G = ili()

    main()
