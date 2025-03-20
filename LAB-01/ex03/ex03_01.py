def  tinh_tong_so_chan(args):
    tong = 0
    for num in args :
        if num % 2 == 0:
            tong += num
    return tong

input_lst = input("Nhap danh sach cac so, cachn nhau bang dau phay: ")
numbers = list(map(int , input_lst.split(',')))

tong_chan = tinh_tong_so_chan(numbers)

print("Tong cac so chan trong list la :", tong_chan)    