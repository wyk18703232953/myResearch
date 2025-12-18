import sys
import threading
inp = sys.stdin.buffer.readline      
input = lambda: sys.stdin.readline().rstrip()
def I(): return list(map(int,inp().split()))
def main():
    n,=I() ; vis=[0]*n ; st=[0]*n
    if n==1:
        print(1)
        exit(0)
    def dfs(g,e):
        if vis[e]==1: return
        else: 
            vis[e]=1
            for i in g[e]:
                dfs(g,i)
            if len(g[e])==1 and e!=0: st[e]+=1
            for i in g[e]:
                st[e]+=st[i]
    a=[int(i)-1 for i in input().split()]
    g=[[] for i in range(n)]
    for i in range(n-1):
        g[i+1].append(a[i])
        g[a[i]].append(i+1)
    dfs(g,0)
    st.sort()
    print(*st)
sys.setrecursionlimit(2097152)
threading.stack_size(134217728)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()