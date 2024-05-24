from Object_class import Hotel
from Object_class import User

ks =[]
u = []
ks1 = Hotel("H1",4,"Bangalore",5,100)
ks.append(ks1)
ks2 = Hotel("H2",5,"Bangalore",5,200)
ks.append(ks2)
ks3 = Hotel("H3",6,"Mumbai",3,100)
ks.append(ks3)
 
u1 = User("U1",2,1000)
u.append(u1)
u2 = User("U2",3,1200)
u.append(u2)
u3 = User("U3",4,1100) 
u.append(u3)

def compare_by_name_user(u):
    return u.User_Name

def compare_by_name_ks(ks):
    return ks.Hotel_Name_Room

def compare_by_rating_ks(ks):
    return ks.Rating

def compare_by_Room_Available_ks(ks):
    return ks.Room_Available

while True:
    print('''chọn chức năng: 
          0. Thoát
          1. Xem danh sách Khách Sạn và Khách Hàng
          2. Thêm thông tin quản lí (Khách hàng hoặc Khách sạn)
          3. Xoá thông tin quản lí (Khách hàng hoặc Khách sạn)
          4. Sửa thông tin quản lí (Khách hàng và Khách sạn)
          5. Sắp xếp theo tên (Khách sạn)
          6. Sắp xếp theo hạng cao nhất (Khách sạn)
          7. In ra dữ liệu khách sạn cho vị trí Bangalore
          8. Sắp xếp theo số phòng tối đa có sẵn (Khách sạn)
          9. In dữ liệu đặt chổ người dùng
          ''')
    chon = input('Bạn chức năng nào:  ')
    if(chon.isdigit()):
        chon = int(chon)
        if(chon == 0):
            break
        elif(chon == 1):
            if len(ks) == 0: print('Hiện tại chưa có khách sạn được thêm')
            else: 
                print('Hotel Data',"\n")
                print("Hotel_Name_Room","   ","Room Available","   ","Location","   ","\tRating","\t","Price per")
                for i in ks:
                    i.display()
                print('User Data',"\n")
                print("User Name","\t","UserID","\t","Booking cost","\n")
                for x in u:
                    x.display()
        elif (chon == 2):
            print('''Vui lòng chọn chức năng: \n\t1. Thêm Khách sạn  \n\t2.Thêm khách hàng ''')
            choose = int(input('Chọn chức năng: '))
            if( choose == 1):
                Hotel_Name = input('Please press hotel name: ')
                Room_Available = int(input('Please press number room available: '))
                Location = input('Please press location of hotel: ')
                Rating = int(input('Please rate the quality of the hotel: '))
                Price = int(input('Please press price of the room: '))
                ks.append(Hotel(Hotel_Name,Room_Available,Location,Rating,Price))
            elif choose == 2: 
                User_Name  = input("Press Username: ")
                User_ID = int(input("Press User ID: "))
                Cost  = int(input("Press yout cost booking room: "))
                u.append(User(User_Name,User_ID,Cost)) 
            else: print("Chọn lại chức năng khác")      
        elif (chon == 3):
                print('''Vui lòng chọn chức năng: \n\t1. Xoá Khách sạn  \n\t2.Xoá khách hàng ''')
                choose = int(input('Chọn chức năng: '))
                if(choose == 1 ):
                    id = input("Nhập Tên phòng: ")
                    for i in ks:
                        if  i.Hotel_Name_Room  == id: 
                            ks.remove(i)                   
                elif choose == 2:
                    UserID = int(input("Nhập ID Khách hàng:"))
                    for x in u:
                        if x.User_ID == UserID:
                            u.remove(x)
                     
                else: print("Chọn lại chức năng")  
        elif (chon == 4):
            print('''Vui lòng chọn chức năng: \n\t1. Sửa thông tin Khách sạn  \n\t2.Sửa thông tin khách hàng ''')
            choose = int(input('Chọn chức năng: '))
            if(choose == 1):
                id = input("Nhập Tên phòng muôn sửa: ")
                for i in ks:
                    if  i.Hotel_Name_Room  == id: 
                        i.set_Hotel_Name(id)
                        i.set_Room_Available(int(input("Please press number room available: ")))
                        i.set_Location(input('Please press location room:  '))
                        i.set_Rating(int(input('Please rate the quanlity of the hotel: ')))
                        i.set_Price_per(int(input('Please press price of the hotel: ')))
            elif choose == 2:
                UserID = int(input("Nhập ID Khách hàng:"))
                for x in u:
                    if x.User_ID == UserID:
                        x.set_User_Name(input("Please press Ussername: "))
                        x.set_Booking_cost(int(input("Please cost your room: ")))
        
            else: print("Chọn lại chức năng")  
        elif (chon == 5):
            sorted_ks = sorted(ks, key=compare_by_name_ks)   
            for ks in sorted_ks:
                print("  ", ks.Hotel_Name_Room, ks.Room_Available, ks.Location, ks.Rating, ks.Price_per)
        elif (chon == 6):
            sorted_ks = sorted(ks, key=compare_by_rating_ks, reverse=True)   
            for ks in sorted_ks:
                print("  ", ks.Hotel_Name_Room, ks.Room_Available, ks.Location, ks.Rating, ks.Price_per)
        elif (chon == 7):
            sorted_ks = sorted(ks, key=compare_by_name_ks)   
            for ks in sorted_ks:
                if (ks.Location == "Bangalore"):
                    print("  ", ks.Hotel_Name_Room, ks.Room_Available, ks.Location, ks.Rating, ks.Price_per)
        elif (chon == 8):
            sorted_ks = sorted(ks, key=compare_by_Room_Available_ks, reverse=True)   
            for ks in sorted_ks:
                print("  ", ks.Hotel_Name_Room, ks.Room_Available, ks.Location, ks.Rating, ks.Price_per)
        elif (chon == 9):
            sorted_user = sorted(u, key=compare_by_name_user)
            for user in sorted_user:
                print("  ", user.User_Name, user.User_ID, user.Booking_cost)
                
            
    else:
        print('Vui lòng chọn lại')






