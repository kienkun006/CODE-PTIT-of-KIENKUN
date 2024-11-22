s= input()

lower = 0 #Khởi tạo biến lưu chữ thường

for i in s:#vòng lặp này sẽ lặp qua từng ký tự trong chuỗi s
    if i.islower(): #kiểm tra xem ký tự i có phải là ký tự thường hay không Nếu đúng biến lower sẽ được tăng lên 1
        lower = lower + 1# len(s) trả về độ dài của chuỗi s

if lower >= len(s) - lower:# #len(s) -lower sẽ tính số lượng ký tự in hoa trong chuỗi (tức là tổng số ký tự trừ đi số ký tự thường)
    print(s.lower())
else:
    print(s.upper())