for _ in range(int(input(""))):  # Số lần kiểm tra
    n = input("")  # Nhập số (dưới dạng chuỗi)
    a = int(n[:2])  # Hai ký tự đầu tiên
    b = int(n[-2:])  # Hai ký tự cuối cùng
    if a == b:
        print("YES")
    else:
        print("NO")