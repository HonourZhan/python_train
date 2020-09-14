def insert_sort(alist):
	for i in range(1,len(alist)):
		for j in range(i,0,-1):
			if alist[j]<alist[j-1]:
				alist[j],alist[j-1]=alist[j-1],alist[j]
			else:
				break
	return alist

if __name__=='__main__':
	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(li)
	li_sort=insert_sort(li)
	print(li_sort )