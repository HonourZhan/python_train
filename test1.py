def bubble(alist):
	n=len(alist)
	for i in range(n-1,0,-1):
		flag=True
		for j in range(i):
			if alist[j]>alist[j+1]:
				alist[j],alist[j+1]=alist[j+1],alist[j]
				flag=False
		if flag==True:
			break

li = [20,15,17,13,11,23,22,27]
print(li)
bubble(li)
print(li)