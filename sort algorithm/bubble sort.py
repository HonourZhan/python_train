from time import perf_counter

def bubble_sort_op(sequence):
	for i in range(len(sequence)-1,0,-1):
		flag=True
		for j in range(i):
			if sequence[j]>sequence[j+1]:
				sequence[j],sequence[j+1]=sequence[j+1],sequence[j]
				flag=False
		if flag==True:
			break
	return sequence
def bubble_sort(sequence):
	for i in range(len(sequence)-1,0,-1):
		for j in range(i):
			if sequence[j]>sequence[j+1]:
				sequence[j],sequence[j+1]=sequence[j+1],sequence[j]
	return sequence
if __name__=='__main__':
	# li = [6,1,2,3,4,5]
	li = [20,15,17,13,11,23,22,27]
	print(li)
	beg1=perf_counter()
	bubble_sort(li)
	end1=perf_counter()
	beg2=perf_counter()
	bubble_sort_op(li)
	end2=perf_counter()
	print(1000*(end1-beg1),1000*(end2-beg2))
	# print(beg1)