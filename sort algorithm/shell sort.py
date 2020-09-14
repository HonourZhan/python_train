def shell_sort(alist):
	n=len(alist)
	gap=n//2
	# gap变为0之前，插入算法执行的次数
	while gap>0:
		# 插入算法，与普通的插入算法区别就是gap步长
		for j in range(gap,n):
			# j=[gap,gap+1,gap+2,...,n-1]
			i=j
			while i>= gap:
				if alist[i]<alist[i-gap]:
					alist[i],alist[i-gap]=alist[i-gap],alist[i]
					i=i-gap
				else:
					break
		# 缩短gap步长
		gap=gap//2
	return alist

if __name__=='__main__':
	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(li)
	li_sort=shell_sort(li)
	print(li_sort )
