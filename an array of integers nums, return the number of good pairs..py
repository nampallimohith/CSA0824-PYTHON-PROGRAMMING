l=[1,2,3,1,1,3]
c=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            print("(",i,j,")")
            c+=1
print("number of good pairs:",c)
