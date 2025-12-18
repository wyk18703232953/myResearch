from math import ceil
def paper(a,b,c,d):
    return ceil((a*(ceil(b/c)))/d)

a,b,c,d=map(int,input().strip().split())
print(paper(a,b,c,d))