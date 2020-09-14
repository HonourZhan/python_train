def select_sort(alist):
	'''选择排序'''
	n=len(alist)
	for i in range(n):
		min_index=i
		for j in range(i+1,n):
			if alist[j]<alist[min_index]:
				min_index=j
		alist[min_index],alist[i]=alist[i],alist[min_index]
	return alist


if __name__=='__main__':
	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(li)
	li_sort=select_sort(li)
	print(li_sort)

