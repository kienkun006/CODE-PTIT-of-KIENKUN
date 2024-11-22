tong=0
x=input()
for i in range(len(x)):
    if x[i]=='4' or x[i]=='7':
        tong+=1
if tong==4 or tong==7:
    print("YES")
else :
    print('NO')