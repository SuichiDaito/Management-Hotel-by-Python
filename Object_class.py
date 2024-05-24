class Hotel: 
    count = 0
    Hotel_Name_Room =""
    Room_Available = 0
    Location = ""
    Rating = 0
    Price_per = 0    
    def __init__(self,Hotel_Name_Room, Room_Available,Location,Rating,Price_per):
        self.Hotel_Name_Room = Hotel_Name_Room
        self.Room_Available = Room_Available
        self.Location = Location
        self.Rating = Rating
        self.Price_per = Price_per
        Hotel.count +=1

    def set_Hotel_Name(self, hotel):
        self.Hotel_Name_Room = hotel

    def get_Hotel_Name(self):
        return self.Hotel_Name_Room
    
    def set_Room_Available(self, number):
        self.Room_Available = number

    def get_Room_Available(self):
        return self.Room_Available
    
    def set_Location(self,local):
        self.Location = local

    def get_Location(self):
        return self.Location
    
    def set_Rating(self,rate):
        self.Rating = rate

    def get_Rating(self):
        return self.Rating
    
    def set_Price_per(self, price):
        self.Price_per = price

    def get_Price_per(self):
        return self.Price_per
        
    def display(self):
        print("\t",self.Hotel_Name_Room,"\t\t",self.Room_Available,"\t","    ",self.Location,"\t"+ "   ",self.Rating,"\t","   " ,self.Price_per)
        print("\n")
        
class User:
    count = 0
    User_Name = ""
    User_ID =0
    Booking_cost = 0
    def __init__(self,User_Name,User_ID,Booking_cost):
        self.User_Name = User_Name
        self.User_ID = User_ID
        self.Booking_cost = Booking_cost
        User.count +=1

    def set_User_Name(self, name) :
        self.User_Name = name

    def get_User_Name(self):
        return self.User_Name
    
    def set_User_ID(self):
        self.User_ID

    def get_User_ID(self):
        return self.User_ID
    
    def set_Booking_cost(self, cost):
        self.Booking_cost = cost

    def get_Booking_cost(self):
        return self.Booking_cost
    
    def display(self):
        print(self.User_Name,"\t\t",self.User_ID,"\t\t",self.Booking_cost)
        print("\n")





