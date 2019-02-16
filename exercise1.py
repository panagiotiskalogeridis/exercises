def sumintervals(li):
    sum=0
    a=len(li)
    for i in range(0,a):
        b=li[i]
        for j in range(b[0]+1,b[1]):
            b.append(j)
        b.sort()
    li[i]=b
    li.sort()
    for i in range (0,a-1):
        for j in range (i+1,a):
            cell1=li[i]
            cell2=li[j]
            l1=len(cell1)
            if cell1[l1-1]>=cell2[0]:
                li[i]=li[i]+li[j]
                li[j]=[0]
    li.sort()
    for j in range (0,a):
        if li[j]!=0:
            cell=li[j]
            cell.sort()
            lcell=len(cell)
            for i in range (1,lcell):
                if cell[i-1]==cell[i]:
                    cell[i-1]=0
                cell.sort()
            li[j]=cell
    fli=[]
    for i in range (0,a):
        lkl=len(li[i])
        kl=li[i]
        if kl[lkl-1]!=0:
            fli.append(li[i])
    lfli=len(fli)
    for i in range (0,lfli):
        presum=0
        k=fli[i]
        lk=len(k)
        j=0
        while j<=lk:
            if k[j]!=0:
                presum=k[lk-1]-k[j]
                j=lk+1
            else:
                j=j+1
        sum=sum+presum
    print sum
