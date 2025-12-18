def decimal_to_26(num):
    num = int(num)
    res = ''
    while num:
        mod = num % 26
        if mod == 0:
            res = 'Z' + res
            num = num // 26 - 1
        else:
            num //= 26
            res = chr(mod+64) + res
    return res

def RXCY_to_Excel(c,r):
    new_row = decimal_to_26(r)
    return new_row + str(c)
# print(RXCY_to_Excel(55,23))

n = int(input())
li = []
for i in range(n):
    li.append(input())
for i in li:
    di_index = []
    al_index = []
    temp = i
    for j in range(len(i)):
        if i[j].isalpha():
            al_index.append(j)
            i = i.replace(i[j],' ')
            # print(i)
        elif i[j].isdigit():
            di_index.append(j)
            i = i.replace(i[j],' ')
            # print(i)
    i = temp
    if min(di_index) < max(al_index): # RxxCxx
        # print(i)
        row = int(i[1:i.index('C')])
        col = int(i[i.index('C')+1:])
        # print(row,col,sep=' ')
        print(RXCY_to_Excel(row,col))
    else: # COL + ROW
        row_num = 0
        for k in range(len(i)):
            if i[k].isdigit():
                num_start = k
                break
        # print(i)
        # print(k)
        length = len(i[0:k])
        # print(length)
        for m in range(num_start):
            row_num += 26 ** (length-1) * (ord(i[m])-64) or (ord(i[m])-64)
            # print(row_num)
            length -= 1
        print('R'+i[num_start:]+'C'+str(row_num))








