def generate_prefix(substring):
	m=len(substring)
	prefix_table=[0]*m
	index=0
	i=1
	while i<m:
		if substring[index]==substring[i]:
			prefix_table[i]=index+1
			index=index+1
			i=i+1
		elif index!=0:
			index=prefix_table[index-1]
		else:
			prefix_table[i]=0
			i=i+1
	prefix_table=[-1]+prefix_table[:m-1]
	return prefix_table

def KMP_search(string,substring):
	# string[i],    len(string)    =m
	# substring[j], len(substring) =n
	m=len(string)
	n=len(substring)
	i,j=0,0
	prefix_table=generate_prefix(substring)
	while i<m and j<n:
		if j == n - 1 and substring[j] == string[i]:
			print('found substring at ', i - j)
			j = prefix_table[j]
		if string[i]==substring[j]:
			i=i+1
			j=j+1
		else:
			j=prefix_table[j]
			if j==-1:
				j=j+1
				i=i+1


if __name__=='__main__':
	# substring='ababc'
	# prefix=generate_prefix(substring)
	# print(prefix)
	string   ='ABABCABAAABABCABAA'
	substring='ABABCABAA'
	KMP_search(string,substring)