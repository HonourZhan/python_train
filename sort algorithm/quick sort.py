def quick_sort(alist,start,end):
	if start>end:
		return
	n=len(alist)
	tar_val=alist[start]
	low=start
	high=end
	while low<high:
		while low<high and alist[high]>tar_val:
			high=high-1
		alist[low]=alist[high]
		while low<high and alist[low]<=tar_val:
			low=low+1
		alist[high]=alist[low]
	alist[low]=tar_val
	quick_sort(alist,start,low-1)
	quick_sort(alist,low+1,end)
	return alist

if __name__=='__main__':
	li = [22, 26, 93, 17, 77, 31, 44, 55, 20]
	print(li)
	li_sort=quick_sort(li,0,len(li)-1)
	print(li_sort)