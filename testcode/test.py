s='a '
for i in range(len(s)-1,-1,-1):
	if s[i]==' ':
		i=i-1
	else:
		break
s=s[:i+1]
if len(s) == 0: print(0)
j = len(s) - 1
while j >= 0 and s[j] != ' ':
	j = j - 1
print(len(s) - 1 - j)