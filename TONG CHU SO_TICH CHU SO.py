for t in range(int(input())):#Nhập số trường hợp cần xử lý

    a = list(int(i) for i in input())
    """input(): đọc một dòng từ đầu vào dưới dạng chuỗi 
    for i in input() :duyệt qua từng ký tự i trong chuỗi đã nhập 
    int(i) : chuyển đổi từng ký tự i (chữ số dưới dạng chuỗi ) thành số nguyên 
    list(int(i) for i in input () :tạo một danh sách gồm các số nguyên từ từng ký tự của chuỗi đã nhập vào """

    su, mu = 0, 0  # su = sẽ dùng để lưu tổng các chữ số ở vị trí chẵn
                   # mu = sẽ dùng để lưu tích các chữ số ở vị trí lẻ

    for i in range(len(a)): #Vòng lặp sẽ duyệt qua từng phần tử trong danh sách s bằng chỉ số i

        if i % 2 == 0: #Nếu là vị trí chẵn thì sẽ cộng giá trị tại vị trí i đó a[i]
            su += a[i]

        else: #Ngược lại là vị trí lẻ
            if a[i] != 0:# kiểm tra nếu giá trị ở vị trí i đó mà khác 0

                if mu == 0: # nếu  tích mà bằng 0 thì biến tích đó sẽ nhận lại giá trị ở vị trí i dó
                     mu = a[i]
                else: # Nếu mu khắc 1 thì biến tích sẽ nhân với
                   mu *= a[i]
    print(str(su) + " " + str(mu)) # in ra kết qua theo dạng chuỗi str_