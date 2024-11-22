def xep(x):
    return (-x[1],x[2],x[0])

n=int(input())
lst=[]
for i in range(n):
    S=input()#Tên sinh viên
    C ,T=map(int,input().split())# C:Số bài làm đúng ,T:Số lượt submit
    lst .append(S,C,T)
lst.sort(key=xep)
for i in lst :
    print(i[0],i[1],i[2])
