class DoubleListNode(object):
	"""双向链表节点"""

	def __init__(self, item):
		self.item = item
		self.next = None
		self.prev = None


class DoubleLinkList(object):
	"""双向链表"""

	def __init__(self):
		self._head = None


	def is_empty(self):
		"""判断链表是否为空"""
		return self._head == None


	def length(self):
		"""返回链表长度"""
		cur=self._head
		count=0
		while cur!=None:
			count=count+1
			cur=cur.next
		return count

	def travel(self):
		'''遍历链表'''
		cur=self._head
		while cur!=None:
			print(cur.item,end=' ')
			cur=cur.next
		print('')

	def add(self,item):
		'''头部插入结点'''
		node=DoubleListNode(item)
		if self.is_empty():
			self._head=node
		else:
			node.next=self._head
			self._head.prev=node
			self._head=node

	def append(self,item):
		'''尾部插入结点'''
		node=DoubleListNode(item)
		cur=self._head
		if self.is_empty():
			self._head=node
		else:
			cur=self._head
			while cur.next!=None:
				cur=cur.next
			cur.next=node
			node.prev=cur

	def search(self,item):
		'''查找元素是否存在'''
		cur=self._head
		while cur!=None:
			if cur.item==item:
				return True
			else:
				cur=cur.next
		return False

	def insert(self,pos,item):
		'''在指定位置插入结点'''
		node=DoubleListNode(item)
		if pos<=0:
			self.add(item)
		elif pos>(self.length()-1):
			self.append(item)
		else:
			cur=self._head
			count=0
			while count<pos:
				count=count+1
				cur=cur.next
			node.prev=cur.prev
			node.next=cur
			cur.prev.next=node
			cur.prev=node

	def remove(self,item):
		'''删除结点'''
		if self.is_empty():
			return
		else:
			cur=self._head
			# 如果要删除的结点为头结点
			if cur.item==item:
				# 如果链表只有一个结点
				if cur.next==None:
					self._head=None
				else:
					cur.next.prev=None
					self._head=cur.next
				return
			while cur!=None:
				if cur.item==item:
					cur.prev.next=cur.next
					if cur.next==None:
						pass
					else:
						cur.next.prev=cur.prev
					break
				cur=cur.next



if __name__ == "__main__":
	ll = DoubleLinkList()
	print(ll.is_empty())
	ll.add(1)
	ll.append(3)
	ll.add(2)
	ll.append(4)
	ll.insert(2,5)
	ll.travel()
	print(ll.length())
	ll.remove(4)
	ll.travel()
	print(ll.length())
