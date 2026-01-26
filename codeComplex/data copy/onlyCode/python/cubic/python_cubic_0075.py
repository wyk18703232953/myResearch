with open("input.txt","r") as in_file: 
    with open("output.txt","a") as out_file:
        N,M = map(int,in_file.readline().split())
        K = int(in_file.readline())
        map_max_dist = [[5000 for i in range(M)] for j in range(N)]
        inputs = list(map(int,in_file.readline().split()))
        p = 0 
        while(p<=K*2-2):
            x,y = inputs[p]-1,inputs[p+1]-1
            for r in range(N):
                for c in range(M):
                    dist = abs(x-r)+abs(y-c)
                    if dist<map_max_dist[r][c]:
                        map_max_dist[r][c] = dist
            p+=2
        max_val = 0 
        max_index = (0,0)
        i,j = 0,0
        for i in range(N):
            for j in range(M):
                if(map_max_dist[i][j]>max_val):
                    max_val = map_max_dist[i][j]
                    max_index = (i,j)
        out_file.write("{} {}".format(max_index[0]+1,max_index[1]+1))
    
        