inp = list(map(int, input().strip().split()))
moves = inp[0]
candiesAtTheEnd = inp[1]

def find(moves, candiesAtTheEnd):
  result = -1
  start = 0
  end = moves-1
  while result!=candiesAtTheEnd:
    #print("start: ",start, ", end: ", end)
    mid=((end-start+1)//2)+start
    #print("mid: ", mid)
    pluses=moves-mid
    minuses=mid
    #print("pluses: ", pluses, ", minuses: ", minuses)
    result=((pluses+1)/2)*pluses
    result=result-minuses
    #print("result: ", result)
    if result==candiesAtTheEnd:
      return minuses
    elif result>candiesAtTheEnd:
      start=mid
    else:
      end=mid
    

result_final=find(moves,candiesAtTheEnd)
print(result_final)
