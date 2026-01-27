d={'purple':'Power','green':'Time','blue':'Space','orange':'Soul','red':'Reality','yellow':'Mind'}
for _ in[0]*int(input()):d.pop(input())
print(len(d),*d.values(),sep='\n')