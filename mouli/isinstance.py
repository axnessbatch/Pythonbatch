a=[10,[20,30],40,50,[60,70,80],90]
b=[]
for x in a:
	if isinstance(x,list):
		for j in x:
			b.append(j)
	else:
		b.append(x)
print b