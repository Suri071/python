l=[1,4,5,3]
n=len(l)
print(l)
k=[]
for i in range(0,n):
    for j in range(i+1,n):
        b=j-i
        le=min(l[i],l[j])
        area=b*le
        k.append(area)
maxarea=max(k)
print(maxarea)
        
