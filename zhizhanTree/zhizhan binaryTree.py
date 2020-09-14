class Node(object):
	'''结点类'''

	def __init__(self, item):
		self.item = item
		self.lchild = None
		self.rchild = None


class Tree(object):
	"""树类"""

	def __init__(self, root=None):
		self.root = root

	def add(self,item):
		# 添加节点
		node=Node(item)
		# 如果数是空，则对根结点赋值
		if self.root == None:
			self.root=node
		else:
			queue=[]
			queue.append(self.root)
			# 对已有节点进行层次遍历
			while queue:
				# 弹出队列第一个元素
				cur=queue.pop(0)
				if cur.lchild == None:
					cur.lchild=node
					return
				elif cur.rchild ==None:
					cur.rchild=node
					return
				else:
					# 如果左右子树都不为空，则加入队列继续判断
					queue.append(cur.lchild)
					queue.append(cur.rchild)

	def breadth_travel(self):
		if self.root is None:
			return
		queue = [self.root]
		while queue:
			cur_node = queue.pop(0)
			print(cur_node.item,end=' ')
			if cur_node.lchild is not None:
				queue.append(cur_node.lchild)
			if cur_node.rchild is not None:
				queue.append(cur_node.rchild)

	def preorder(self,node):
		'''先序遍历'''
		res=[]
		if node is None:
			return
		res.append(node.item)
		print(node.item,end=' ')
		self.preorder(node.lchild)
		self.preorder(node.rchild)
		# print('res=',res)

	def inorder(self,node):
		'''中序遍历'''
		if node is None:
			return
		self.inorder(node.lchild)
		print(node.item, end=' ')
		self.inorder(node.rchild)

	def postorder(self,node):
		'''后序遍历'''
		if node is None:
			return
		self.postorder(node.lchild)
		self.postorder(node.rchild)
		print(node.item,end=' ')



if __name__ == "__main__":
	tree = Tree()
	tree.add(0)
	tree.add(1)
	tree.add(2)
	tree.add(3)
	tree.add(4)
	tree.add(5)
	tree.add(6)
	tree.add(7)
	tree.add(8)
	tree.add(9)
	tree.breadth_travel()
	print('')
	tree.preorder(tree.root)
	print('')
	tree.inorder(tree.root)
	print('')
	tree.postorder(tree.root)

