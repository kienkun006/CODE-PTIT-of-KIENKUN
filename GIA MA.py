for t in range(int(input())):#Nhập số bộ test

    s = input()#Nhập chuỗi s theo định dạng

    res = ''#Khởi tạo một chuỗi rỗng để lưu kết quả sau xử lý

    for i in range(0, len(s), 2):#Vòng lặp sẽ chạy giá trị từ 0 đến len(s)-1 với step=2
        res += s[i] * int(s[i + 1])# vòng lặp cộng chuỗi res nối đôi và xử lý theo cặp với mỗi giá trị i đi qua

    print(res)
