class Node(object):
	def __init__(self,item):
		self.item=item
		self.next=None

class SinCycLinkedlist(object):

	"""单向循环链表"""
	def __init__(self):
		self._head=None

	"""判断链表是否为空"""
	def is_empty(self):
		return self._head==None

	"""返回链表的长度"""
	def length(self):
		if self.is_empty():
			return 0
		count=1
		cur=self._head
		while cur.next!=self._head:
			count=count+1
			cur=cur.next
		return count

	'''遍历链表'''
	def travel(self):
		if self.is_empty():
			return
		cur=self._head
		print(cur.item,end=' ')
		while cur.next!=self._head:
			cur=cur.next
			print(cur.item, end=' ')

	'''在链表头部添加结点'''
	def add(self,item):
		node=Node(item)
		if self.is_empty():
			self._head=node
			node.next=self._head
		else:
			node.next=self._head
			cur=self._head
			while cur.next!=self._head:
				cur=cur.next
			cur.next=node
			self._head=node

	'''尾部添加结点'''
	def append(self,item):
		node=Node(item)
		if self.is_empty():
			self._head=node
			node=self._head
		else:
			cur=self._head
			while cur.next!=self._head:
				cur=cur.next
			cur.next=node
			node.next=self._head

	'''在指定位置插入结点'''
	def insert(self,pos,item):
		if pos<=0:
			self.add(item)
		elif pos>(self.length()-1):
			self.append(item)
		else:
			count=0
			node=Node(item)
			cur=self._head
			while count<(pos-1):
				cur=cur.next
				count=count+1
			node.next=cur.next
			cur.next=node

	'''删除一个结点'''
	def remove(self,item):
		# 若链表为空，则返回空值
		if self.is_empty():
			return
		cur=self._head
		pre=None
		# 若头节点的元素就是要查找的元素item
		if cur.item==item:
			# 如果链表不止一个节点
			if cur.next!=self._head:
				# 先找到尾节点，将尾节点的next指向第二个节点
				while cur.next!=self._head:
					cur=cur.next
				# cur指向了尾节点
				cur.next=self._head.next
				self._head=self._head.next
			else:
				# 链表只有一个节点
				self._head=None
		else:
			# 第一个节点不是要删除的
			pre=self._head
			while cur.next!=self._head:
				# 找到了要删除的元素
				if cur.item==item:
					pre.next=cur.next
					return
				else:
					pre=cur
					cur=cur.next
			# cur 指向尾节点
			if cur.item==item:
				pre.next=cur.next
	def search(self,item):
		if self.is_empty():
			return False
		cur=self._head
		if cur.item==item:
			return True
		while cur.next!=self._head:
			if cur.item==item:
				return True
			else:
				cur=cur.next
		return False

if __name__ == "__main__":
    ll = SinCycLinkedlist()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print ("length:",ll.length())
    ll.travel()
    print (ll.search(3))
    print (ll.search(7))
    ll.remove(1)
    print ("length:",ll.length())
    ll.travel()


