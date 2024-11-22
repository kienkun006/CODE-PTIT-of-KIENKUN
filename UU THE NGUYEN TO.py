import math

#Tạo hàm kiểm tra số nguyên số
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1
#Vòng lặp chính và xử lý liệu đầu vào
for t in range(int(input())): #Nhập số trường hợp cần xử lý
    s = input() #Nhập chuỗi
    l, nt = len(s), 0# l = chiều dài của chuỗi s ; nt =biến đếm số nguyên tố trong chuỗi s
    for i in s: #Vòng lặp for để duyệt từng chữ số trong chuỗi s
        if isPrime(int(i)): #Mỗi chữ số đấy được chuyển sang thành kiểu số nguyên ,và sau đó truyền vào hàm isPrime để kiểm tra có phải số nguyên ko
            nt += 1 #Nếu là số nguyên thì biến đếm sẽ được tăng lên 1
    print('YES' if isPrime(l) and nt > l - nt else 'NO')
   #isPrime(l) kiểm tra xem chiều dài chuỗi s có phải số nguyên tố ko (YÊU CẦU 1)
   #nt > l - nt kiểm tra xem số lượng chữ số nguyên tố có nhiều hơn chữ số ko nguyên tố ko (YÊU CẦU 2)
   #nt là chữ số nguyên tố trong chuỗi
   #l - nt là chữ số ko phải nguyên tố
