from QuanLySinhVien import QuanLySinhVien

def main():
    QuanLySinhVien = QuanLySinhVien()
    
    while True:
        print("\n====== QUẢN LÝ SINH VIÊN ======")
        print("1. Thêm sinh viên")
        print("2. Cập nhật sinh viên")
        print("3. Xóa sinh viên")
        print("4. Hiển thị danh sách sinh viên")
        print("5. Sắp xếp theo ID")
        print("6. Sắp xếp theo tên")
        print("7. Sắp xếp theo điểm trung bình")
        print("8. Tìm sinh viên theo ID")
        print("9. Tìm sinh viên theo tên")
        print("0. Thoát")
        
        choice = input("Nhập lựa chọn: ")

        if choice == "1":
            QuanLySinhVien.nhapSinhVien()
        
        elif choice == "2":
            ID = int(input("Nhập ID sinh viên cần cập nhật: "))
            QuanLySinhVien.updateSinhVien(ID)
        
        elif choice == "3":
            ID = int(input("Nhập ID sinh viên cần xóa: "))
            if QuanLySinhVien.deleteById(ID):
                print("Xóa thành công!")
            else:
                print("Không tìm thấy sinh viên!")
        
        elif choice == "4":
            QuanLySinhVien.showSinhVien()
        
        elif choice == "5":
            QuanLySinhVien.sortByID()
            print("Đã sắp xếp theo ID!")
        
        elif choice == "6":
            QuanLySinhVien.sortByName()
            print("Đã sắp xếp theo tên!")
        
        elif choice == "7":
            QuanLySinhVien.sortDiemTB()
            print("Đã sắp xếp theo điểm trung bình!")
        
        elif choice == "8":
            ID = int(input("Nhập ID sinh viên cần tìm: "))
            sv = QuanLySinhVien.findByID(ID)
            if sv:
                QuanLySinhVien.showSinhVien([sv])
            else:
                print("Không tìm thấy sinh viên!")
        
        elif choice == "9":
            name = input("Nhập tên sinh viên cần tìm: ")
            listSV = QuanLySinhVien.findByName(name)
            if listSV:
                QuanLySinhVien.showSinhVien(listSV)
            else:
                print("Không tìm thấy sinh viên!")
        
        elif choice == "0":
            print("Thoát chương trình. Hẹn gặp lại!")
            break
        
        else:
            print("Lựa chọn không hợp lệ! Vui lòng nhập lại.")

if __name__ == "__main__":
    main()
