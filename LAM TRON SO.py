
for t in range (int(input())):#Nhập số trường hợp kiểm tra

    arr =[int(s) for s in input()]#Nhập một chuỗi  --> tách từng ký tự trong chuỗi thành kiểu int và lưu trong list
#Vòng for chạy ngược từ cuối dãy về đầu dãy
    for i in range(len(arr)-1,0,-1):

        if arr[i] >=5 :
            arr[i-1]+=1 #chữ số ngay bên trái sẽ cộng 1

        arr[i]=0 #chữ số hiện tại sẽ trở thành 0
        # (Vẫn thực hiện dù if trên ko thỏa mãn ,để đảm bảo các chữ số bên phải khi làm tròn là số 0)

    if arr[0]==10: #nếu chữ số đầu tiên bằng 10
        arr[0]=0#Thì sẽ chuyển thành 0
        arr=[1]+arr#Cộng thêm [1] vào đầu list arr

    for i in arr :#Chạy vòng để in từng chữ số trong arr mà ko xuống dòng
        print(i,end="")
    print()