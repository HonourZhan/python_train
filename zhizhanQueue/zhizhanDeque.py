class Deque(object):
	'''双端队列'''

	def __init__(self):
		self.__list=[]

	def add_front(self,item):
		'''往队列头部添加元素'''
		self.__list.insert(0,item)

	def add_rear(self,item):
		'''往队列尾部添加元素'''
		# inser函数为在对应目标之前添加元素，因而不能使用self.__list.insert(-1,item)这种形式
		self.__list.append(item)

	def pop_front(self):
		'''从队列头部删除元素'''
		return self.__list.pop(0)

	def pop_rear(self):
		'''从队列尾部删除元素'''
		return self.__list.pop()

	def is_empty(self):
		'''判断双端队列是否为空'''
		return self.__list==None

	def size(self):
		return len(self.__list)

if __name__=='__main__':
	s=Deque()
	s.add_front(1)
	s.add_front(3)
	s.add_rear(2)
	s.add_rear(4)
	print('双端队列长度为：',s.size())
	print(s.pop_front())
	print(s.pop_front())
	print(s.pop_front())
	print(s.pop_front())