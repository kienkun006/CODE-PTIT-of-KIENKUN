import math # sử dụng thư viện toán học để dễ sử dụng

for t in range(int(input())):#Số trường hợp cần xử lý

    n ,x ,m=[float(i) for i in input().split()]#Nhập giá trị của n,x,m với i là kiểm float
    #khi nhập thì sẽ dử dụng split để tách các giá trị input thành các list rồi lặp để gán các giá trị vào n ,x,m

    res = math.log(m/n,1+x/100) #Công thức biến đổi log

    print(math.ceil(res)) #In ra giá trị trần của res Bởi vì thời gian phải làm tròn thành số nguyên lớn hơn gần nhất