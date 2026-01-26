import sys
def ask(x,y,rev):
	if (rev==0):
		print("? %d %d"%(x,y))
	else:
		print("? %d %d"%(y,x))
	sys.stdout.flush()
	if (rev==1):
		return -int(input())
	else:
		return int(input())

comp=ask(0,0,0)
nowa=0
nowb=0
rev=0
for i in range(29,-1,-1):
	if (comp<0):
		rev^=1
		nowa,nowb=nowb,nowa
		comp=-comp
	if comp>=0:
		comp=ask(nowa|(1<<i),nowb|(1<<i),rev)
		if (comp<0):
			nowa|=1<<i
			comp=ask(nowa,nowb,rev)
		else:
			tmp=ask(nowa|(1<<i),nowb,rev)
			if (tmp<0):
				nowa|=1<<i
				nowb|=1<<i
if (rev==1):
	nowa,nowb=nowb,nowa
print("! %d %d"%(nowa,nowb))
			
		