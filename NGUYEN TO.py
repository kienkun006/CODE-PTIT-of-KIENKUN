##Số nguyên tố là só chỉ có 2 ước là : 1 và chính nó
#Do vậy nếu không phải số nguyên tố thì sẽ có ít nhất một ước khắc ngoài 2 ước trên
#Kiếm tra n thì ta sẽ chỉ cần kiểm tra từ giá trị 2 đến căn bậc 2 của n
"""VD n=36 thì sẽ có những ước là : 1,2,3,4,6,9,12,18,36
      căn bặc 2 của n (36) là 6
      Để giảm số lần lặp kiếm tra,tăng hiệu suất thì ta chỉ cần cho chạy tới căn bậc 2 của 36
      Ta sẽ đi kiểm tra 2,3,4,5,6 thì ta thấy
      2 chia hết cho 36 (không phải nguyên tố). 36=18*2
      3 chia hết cho 36 (không phải nguyên tố). 36=12*3
      4 chia hết cho 36 (không phải nguyên tố). 36=9*4
      5 không chia hết (có thể là nguyên tố, nhưng không cần kiểm tra thêm vì đã có số chia hết).
      6 chia hết cho 36 (không phải nguyên tố). 36=6*6"""
#Nhận xét :Nếu n= a x b trong đó a và b là có ước số của n thì ít nhất 1 trong 2 số đó phải nhỏ hơn hoặc bằng căn bậc 2 của n
import math
def is_prime(n): #Xây dựng hàm để kiểm tra số nguyên tố cho k
    if n<1 :
        return False
    for i in range ( 2,int(math.sqrt(n)+1)):
        if n%i ==0:
            return False
    return n>1
#Vòng lặp chính
for x in range (int(input())):#Số trường hợp kiểm tra
    n=int(input()) #Nhập số n
    k=0
    for i in range (1,n):# vòng lặp giá trị 1,2,3....n để tìm coprime của n
        if math.gcd(i,n)==1: #tìm coprime của (i,n) nếu thỏa mã thì mỗi lần tm k+1
            k=k+1
        if (is_prime(k)):#kiểm tra xem k có phải số nguyên tố ko
            print("YES")
        else:
            print("NO")



