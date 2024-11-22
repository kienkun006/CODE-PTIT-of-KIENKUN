for t in range (int(input())):#Tạo bộ test
    s=input()+"!" #Đọc chuỗi và thêm ký tự kết thúc
    cnt,ch=0,s[0] #Tạo biến cnt : là biến số lần ký tự lập lại ,ch : là ký tự hiện tại
    for i in s: #Vòng lặp các ký tự trong chuỗi s
        if i==ch: #Nếu ký tự i trong s = ký tự hiện tại
            cnt+=1
        else:#Ngược lại
            print(str(cnt) + ch,end='')#In ra số lần ký tự lặp và ký tự đó
            cnt=1
            ch=i
    print()
