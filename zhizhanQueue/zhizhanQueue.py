class Queue(object):
	'''队列'''
	def __init__(self):
		self.item=[]

	def enqueue(self,item):
		'''往队列尾部添加一个item元素'''
		self.item.append(item)

	def dequeue(self):
		'''从队列头部删除一个元素'''
		if self.item:
			return self.item.pop(0)
		else:
			return None

	def is_empty(self):
		'''判断队列是否为空'''
		return self.item==[]

	def size(self):
		'''返回队列的大小'''
		return len(self.item)

'''测试代码'''
if __name__=='__main__':
	s = Queue()
	print(s.is_empty())
	s.enqueue(1)
	s.enqueue(2)
	s.enqueue(3)
	s.enqueue(4)
	print('队列长度为：',s.size())
	# print(s.peek())
	# s.travel()
	print(s.dequeue())
	print(s.dequeue())
	print(s.dequeue())
	print(s.dequeue())
	print(s.dequeue())