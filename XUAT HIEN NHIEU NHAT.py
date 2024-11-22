for t in range (int(input())):
    n= int(input()) #nhập giá tr cho n
    b=[int(i) for i in input().split()]
    a={}#tạo một list để đếm phần tử trong b
    for x in b :
        if x in a:
            a[x]+=1 #nếu đã cuất hiện trong list thì a[x] sẽ tăng thêm 1 đơn vị
        else:
            a[x]=1# nếu x chưa có tronbg a gán giá trị a[x] bằng 1

    check=0
    for i,j in a.items():
        if j > n//2 :#kiểm tra giá tri value nào lớn hơn n/2 theo đề bài
            check=1
            print(i)
            break
    if check==0:
        print("NO")
