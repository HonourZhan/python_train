class SingleNode(object):
	# 节点类
	def __init__(self, item):
		self.item = item  # 存放数据元素
		self.next = None  # 下一个结点的标识


class SingleLinkList(object):
	'''单链表'''

	def __init__(self):
		self._head = None

	'''判断链表是否为空'''

	def is_empty(self):
		return self._head == None

	'''链表长度'''

	def length(self):
		cur=self._head
		count=0
		while cur!=None:
			count=count+1
			cur=cur.next
		return count

	'''遍历链表'''

	def travel(self):
		cur=self._head
		while cur!=None:
			print(cur.item,end=' ')
			cur=cur.next
		print(' ')

	'''头部添加元素'''

	def add(self, item):
		node = SingleNode(item)  # 先创建一个结点保存item的值
		node.next = self._head  # 将新结点的next指向头节点，即_head指向的位置
		self._head = node  # 将链表的头结点指向新结点

	'''尾部添加元素'''

	def append(self, item):
		node = SingleNode(item)
		# 先判断链表是否为空，若是空链表，则将_head指向新节点
		if self.is_empty():
			self._head = node
		else:
			cur = self._head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			node.next=None

	'''指定位置添加元素'''

	def insert(self,pos,item):
		node=SingleNode(item)
		# 若指定插入位置为第一个结点之前，则为头插，可使用add函数
		if pos<=0:
			self.add(item)
		# 若指定插入位置为最后一个结点之后，则为尾插，可使用append函数
		elif pos>(self.length()-1):
			self.append(item)
		# 寻找插入位置
		else:
			count=0
			prior=self._head
			while count<(pos-1):
				count=count+1
				prior=prior.next
			# 当循环退出后，prior指向pos-1位置处
			node.next=prior.next
			prior.next=node

	'''删除结点'''

	def remove(self,item):
		cur=self._head
		pre=None
		while cur!=None:
			if cur.item==item:
				# 先判断此结点是否为头结点
				if cur==self._head:
					self._head=self._head.next
				else:
					pre.next=cur.next
				break
			else:
				pre=cur
				cur=cur.next

	'查找结点是否存在'

	def search(self,item):
		cur=self._head
		while cur!=None:
			if cur.item==item:
				return True
			else:
				cur=cur.next
		return False

'''测试代码'''
if __name__ == "__main__":
	ll = SingleLinkList()
	ll.append(1)
	print(ll.is_empty())
	print(ll.length())
	ll.travel()

	ll.append(2)
	ll.add(8)
	ll.append(3)
	ll.append(4)
	ll.insert(-1, 9)
	ll.travel()
	print('链表长度为：', ll.length())
	ll.insert(2, 100)
	ll.travel()
	ll.insert(10, 200)
	ll.travel()
	ll.remove(9)
	ll.travel()
	ll.remove(200)
	ll.travel()
	print(ll.search(8))
