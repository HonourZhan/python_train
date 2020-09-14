class Stack(object):
	'''栈'''
	def __init__(self):
		self.item=[]

	def push(self,item):
		'''添加一个新的元素item到栈顶'''
		self.item.append(item)

	def pop(self):
		'''弹出栈顶元素'''
		if self.item:
			return self.item.pop()
		else:
			return None

	def peek(self):
		'''返回栈顶元素'''
		if self.item:
			return self.item[-1]
		else:
			return None

	def is_empty(self):
		'''判断栈是否为空'''
		return self.item==[]

	def size(self):
		'''返回栈的元素个数'''
		return len(self.item)

	def travel(self):
		for i in range((self.size())):
			print(self.item[self.size()-1-i],end=' ')
		print('')

if __name__=='__main__':
	s = Stack()
	print(s.is_empty())
	s.push(1)
	s.push(2)
	s.push(3)
	s.push(4)
	print('队列长度为：',s.size())
	# print(s.peek())
	# s.travel()
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.pop())