dictionary={}
while(True):#In bảng menu lựa chọn
    print("*****Menu*****")
    print("1.Thêm từ vừng")
    print("2.Tra cứu từ vựng")
    print("3.Cập nhật ý nghĩa")
    print("4.Xóa 1 từ vựng")
    print("5.Xóa toàn bộ từ vựng")
    print("6.In toàn bộ từ vựng")
    print("7.Kết thúc chương trình")
    luachon=int(input("Hãy chọn Chức năng :"))
    if luachon==1 or luachon==3 :
        x=str(input())#Nhập từ vựng
        y=str(input())#Nhập ý nghĩa
        dictionary.update({x:y})#Cập nhập vào từ điển
        print(dictionary)

    elif luachon==2:
        x=str(input("Nhập từ vựng :"))#nhập từ vựng
        KQ=dictionary[x]#tìm nghĩa của từ vựng
        print("Ý nghĩa :",KQ)

    elif luachon==4:
        x=str(input())#Nhập từ vựng muốn xóa
        dictionary.pop (x)#Xóa khỏi từ điển
        print(dictionary)

    elif luachon==5:
        dictionary.clear()#xóa hết từ điển
        print(dictionary)

    elif luachon==6:
        for x,y in dictionary.items():#in cả từ vựng và nghĩa
            print(x,":",y)
    else:
        print("Chương trình kết thúc""")
        break