c = 0
def backtracking(actuales,restantes,l,r,x):
    global c
    if sum(actuales)<=r and sum(actuales) >= l:
        if max(actuales)- min(actuales) >= x:
            c += 1
    if restantes:
        for i in range(len(restantes)):
            backtracking(actuales+[restantes[i]], restantes[i+1:],l,r,x)
    return 0
def main():
    n,l,r,x = input().split(" ")
    n,l,r,x = int(n), int(l), int(r), int(x)
    difficulties = input().split(" ")
    for i in range(len(difficulties)):
        difficulties[i] = int(difficulties[i])
    difficulties.sort()
    backtracking([],difficulties,l,r,x) 
    global c     
    return c
 
if __name__ == "__main__":
    print(main())