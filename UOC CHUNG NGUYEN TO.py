import math
 #Xây hàm kiểm tra nguyên tố
def isPrime (n):
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return n>1
#Vòng xử lý chính
for t in range (int(input())):

    a,b=[int(i) for i in input().split()]#sẽ nhập 2 giá trị a và b vào
    #Giá trị này sẽ được lập và chia theo khoảng trắng và lưu vào 1 list với giá trị nguyên

    gcd_sum=sum(int(i) for i in str(math.gcd(a,b))) #Tính tổng các chữ số của ước chung lớn nhất của a và b

    if isPrime( gcd_sum):#Kiểm tra tổng của gcd có phải số nguyên tố ko
        print("YES")
    else:
        print("NO")
        