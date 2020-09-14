class SingleNode(object):
	'''定义单节点'''
	def __init__(self,item):
		self.item=item
		self.next=None


class CySingleList(object):
	'''单向循环表'''
	def __init__(self):
		self._head=None


	def is_empty(self):
		'''判断链表是否为空'''
		return self._head==None


	def length(self):
		'''返回链表长度'''
		if self.is_empty():
			return 0
		count=1
		cur=self._head
		while cur.next!=self._head:
			count=count+1
			cur=cur.next
		return count


	def travel(self):
		'''遍历链表'''
		cur=self._head
		if self.is_empty():
			return
		else:
			print(cur.item,end=' ')
			while cur.next!=self._head:
				cur=cur.next
				print(cur.item, end=' ')
			print('')


	def add(self,item):
		'''链表头部插入结点'''
		node=SingleNode(item)
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


	def append(self,item):
		'''链表尾部插入结点'''
		node=SingleNode(item)
		if self.is_empty():
			self._head=node
			node.next=node
		else:
			cur=self._head
			while cur.next!=self._head:
				cur=cur.next
			cur.next=node
			node.next=self._head


	def insert(self,pos,item):
		'''链表指定位置插入结点'''
		if pos<=0:
			self.add(item)
		elif pos>(self.length()-1):
			self.append(item)
		else:
			node=SingleNode(item)
			count=0
			cur=self._head
			while count<(pos-1):
				count=count+1
				cur=cur.next
			node.next=cur.next
			cur.next=node


	def remove(self,item):
		'''移除链表指定元素'''
		# 空链表情况
		if self.is_empty():
			return
		else:
			cur=self._head
			pre=None
			# 若头结点即为要删除的结点
			if cur.item==item:
				# 如果链表只有一个结点
				if cur.next==self._head:
					self._head=None
				# 链表不止一个结点
				else:
					while cur.next!=self._head:
						cur=cur.next
					self._head=self._head.next
					cur.next=self._head
			else:
				pre=cur
				while cur.next!=self._head:
					if cur.item==item:
						pre.next=cur.next
						break
					else:
						pre=cur
						cur=cur.next

	def search(self,item):
		'''链表中搜索结点'''
		if self.is_empty():
			return False
		else:
			cur=self._head
			# 链表头结点即为要搜索的结点
			if cur.item==item:
				return True
			else:
				while cur.next!=self._head:
					cur = cur.next
					if cur.item==item:
						return True
		return False



if __name__=="__main__":
	ll=CySingleList()
	print(ll.is_empty())
	ll.add(2)
	ll.append(3)
	ll.append(1)
	ll.append(3)
	ll.insert(1,5)
	ll.travel()
	print('链表长度为：',ll.length())
	ll.remove(3)
	ll.travel()
	print('链表长度为：',ll.length())
	# print(ll.search(4))

