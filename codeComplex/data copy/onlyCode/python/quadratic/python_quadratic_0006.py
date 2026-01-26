import math
def C1():
    n, r = map(int, input().split())
    x_cord = [int(x) for x in input().split()]

    y_cord = []
    # y cordinate of contacted Disk
    contactedDisk = 0
    for i, x in enumerate(x_cord):
        if len(y_cord) == 0:
            y_cord.append(r)
        else:
            y_cord.append(r)
            for j in range(i):
                diff = abs(x_cord[i] - x_cord[j])
                if diff <= 2 * r:
                    y_cord[i] = max(y_cord[i], math.sqrt(4*r*r - diff ** 2) + y_cord[j])


    for i in y_cord:
        print(i, end= " ")


if __name__=='__main__':
    C1()
	   				    								 		  	  	 	