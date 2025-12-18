import math

def main():
    buf = input()
    n = int(buf)
    buf = input()
    buflist = buf.split()
    a = []
    for i, item in enumerate(buflist):
        a.append([i+1, int(item)])
    a = list(reversed(list(sorted(a, key = lambda x:x[1]))))
    one_deg_count = 0
    for i in a:
        if i[1] == 1:
            one_deg_count += 1
    if one_deg_count == len(a): # only 1-degree vertices
        if one_deg_count == 2:
            print("YES", 1) # result, diameter
            print(1) # edge count
            print(1, 2) # edge info
        else:
            print("NO")
        return
    elif one_deg_count == len(a) - 1: # one multi-degree vertex and n-1 1-degree vertices
        if one_deg_count <= a[0][1]:
            print("YES", 2) # star-shaped graph
            print(one_deg_count)
            for i in range(one_deg_count):
                print(a[0][0], a[-i-1][0])
        else:
            print("NO")
        return
    else: # more than one multi-degree vertices
        spare_edges = 2
        for i in range(len(a) - one_deg_count):
            spare_edges += a[i][1] - 2
        if spare_edges >= one_deg_count:
            diameter = len(a) - 1 - one_deg_count + min(one_deg_count, 2)
            edge_count = 0
            edge_list = []
            for i in range(len(a) - one_deg_count - 1):
                edge_list.append((a[i][0], a[i+1][0]))
            for i in range(len(a) - one_deg_count):
                a[i][1] -= 2
            if one_deg_count > 0:
                edge_list.append((a[0][0], a[-1][0]))
                one_deg_count -= 1
            if one_deg_count > 0:
                edge_list.append((a[-one_deg_count-2][0], a[-2][0]))
                one_deg_count -= 1
            idx = 0
            for i in range(one_deg_count):
                edge_list.append((a[idx][0], a[-i-3][0]))
                a[idx][1] -= 1
                if a[idx][1] <= 0:
                    idx += 1
            print("YES", diameter)
            print(len(edge_list))
            for i in edge_list:
                print(i[0], i[1])
        else:
            print("NO") # impossible

if __name__ == '__main__':
    main()
