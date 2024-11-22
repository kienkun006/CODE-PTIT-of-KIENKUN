#Đầu cuối nguyên tố
import math

#Hàm Kiểm tra số nguyên tố
def ifPrime (n):
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return False
    return    n>1

#Bo test theo yêu cầu
for  x in range(int(input())):
    n=input()
    k=int(n[:3])
    j=int(n[-3:])
    if nguyento(k) and nguyento(j):
        print("YES")
    else:
        print('NO')