import re

# Khởi tạo chuỗi để lưu đầu vào
doc = ""
while True:
    try:
        doc += input() + "\n"  # Thêm mỗi dòng vào doc, kết thúc bằng newline
    except EOFError:  # Kết thúc khi không còn đầu vào
        break

# Tách câu thành danh sách bằng regex
sen = re.split(r'[?.!]', doc)  # Tách câu bằng dấu chấm, hỏi, hoặc dấu chấm than

# Xử lý từng câu
for k in sen:
    k = k.strip()  # Loại bỏ khoảng trắng ở đầu và cuối câu
    if len(k) == 0:
        continue  # Bỏ qua nếu câu rỗng
    chuoi = k.lower().split()  # Chuyển thành chữ thường và tách thành từ
    chuoi[0] = chuoi[0].capitalize()  # Viết hoa ký tự đầu tiên
    print(" ".join(chuoi))  # Nối lại thành câu và in ra