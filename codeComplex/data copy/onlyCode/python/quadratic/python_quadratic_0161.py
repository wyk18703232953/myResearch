import atexit
import io
import sys

# Buffering IO
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
    

def main():
    n, k = [int(x) for x in input().split()]
    p = [int(x) for x in input().split()]
    t = []
    g={}
    for x in p:
        if x in g:
            t.append(g[x])
            continue
        kk = x - 1
        while True:
            if kk in g:
                if x - g[kk] < k:
                    ttt = g[kk]
                else:
                    ttt= kk + 1
                for i in range(kk +1 , x + 1):
                    g[i] = ttt
                t.append(g[x])
                break
            elif kk<0 or x - kk == k:
                for i in range(kk +1 , x + 1):
                    g[i] = kk + 1
                t.append(g[x])
                break
            kk -= 1
            
    print(' '.join((str(x) for x in t)))
            
    
if __name__ == '__main__':
    main()
        