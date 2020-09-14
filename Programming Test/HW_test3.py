def candy(m,i,string,n):
    global z
    if m==0 and len(string)<=n:
        z+=1
        #print(string)  #展示出具体符合条件的示例,方便检查
    else:
        if i>1:
             candy(m,i-1,string,n)
        if i<=m:
             candy(m-i,i,str(i)+''+string,n)

m=int(input(""))
if m<=0 or m>10:
    print("input wrong")
    exit(0)
n=int(input(""))
if n<=0 or n>10:
    print("input wrong")
    exit(0)
i=m
z=0
candy(m,i,'',n)
print(z)#打印出满足次数
