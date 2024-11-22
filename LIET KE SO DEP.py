#Tạo một hàm check() để kiểm tra chiều dài chẵn ,số đối xứng ,chữ số chẵn
def check(s):#Đấu vào yêu cầu kiểu dữ liệu chuỗi str

    if len(s)%2==1 or s != s[::-1]:# Nếu chiều dài s là lẻ hoặc không phải số đối xứng
        return False
    for i in s:#Nếu là chữ số lẻ
        if int(i)%2==1: #Khi kiểm tra chẵn lẻ thì phải là kiểu int
            return False
    return True


for t in range(int(input())):
     n=int(input())

     for i in range(22, n ,2):#vòng lặp từ 22 đến n-1 với step 2 để đảm bảo là số chẵn
         if check(str(i)): #Hàm check nhận kiểu str
             print(i,end=" ")
     print()

