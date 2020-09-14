str_full=input().lower()
str_shor=input().lower()
res=0
for i in range(len(str_full)):
	if str_shor==str_full[i]:
		res=res+1
	else:
		continue
print(res)

