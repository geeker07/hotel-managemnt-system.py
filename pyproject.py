import random
import datetime

name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
roomno = []
custid = []
day = []
p = []

i = 0

def Home():
    print("\t\t\t\t\t\t WELCOME TO HOTEL UPESTAYS\n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Rooms Info\n")
    print("\t\t\t 3 Record\n")
    print("\t\t\t 0 Exit\n")

    try:
        ch = int(input("->"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        Home()

    if ch == 1:
        print(" ")
        Booking()
    elif ch == 2:
        print(" ")
        Rooms_Info()
    elif ch == 3:
        print(" ")
        Record()
    else:
        exit()


def date(c):
    try:
        if c[2] >= 2024 and c[2] <= 2025:
            if c[1] != 0 and c[1] <= 12:
                if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                    if c[2] % 4 == 0 and c[0] <= 29:
                        pass
                    elif c[0] < 29:
                        pass
                    else:
                        raise ValueError("Invalid date")
                elif c[1] <= 7 and c[1] % 2 != 0 and c[0] <= 31:
                    pass
                elif c[1] <= 7 and c[1] % 2 == 0 and c[0] <= 30 and c[1] != 2:
                    pass
                elif c[1] >= 8 and c[1] % 2 == 0 and c[0] <= 31:
                    pass
                elif c[1] >= 8 and c[1] % 2 != 0 and c[0] <= 30:
                    pass
                else:
                    raise ValueError("Invalid date")
            else:
                raise ValueError("Invalid date")
        else:
            raise ValueError("Invalid date")
    except ValueError as e:
        print("Error:", e)
        exit()


def Booking():
    global i
    print(" BOOKING ROOMS")
    print(" ")

    while True:
    
         n = str(input("Name: "))
         phn = str(input("Phone No.: "))
         ADD = str(input("Address: "))
       
         if n == " " or phn== " " or ADD == " ":
            print("\tName, Phone no. & Address cannot be empty..!!")
         else:
            name.append(n)
            add.append(ADD)
            break

    try:
        cin = str(input("Check-In (DD/MM/YYYY): "))
        checkin.append(cin)
        cin = cin.split('/')
        ci = [int(x) for x in cin]
        date(ci)

        cot = str(input("Check-Out (DD/MM/YYYY): "))
        checkout.append(cot)
        cot = cot.split('/')
        co = [int(x) for x in cot]

        if co[1] < ci[1] and co[2] < ci[2]:
            print("\n\tErr..!!\n\t Invalid date\n")
            exit()
        elif co[1] == ci[1] and co[2] >= ci[2] and co[0] <= ci[0]:
            print("\n\tErr..!!\n\t Invalid date\n")
            exit()
        else:
            pass

        date(co)
        d1 = datetime.datetime(ci[2], ci[1], ci[0])
        d2 = datetime.datetime(co[2], co[1], co[0])
        d = (d2 - d1).days
        day.append(d)

        print("\t\tROOM TYPE'S\t\t")
        print(" 1. Standard Non-AC")
        print(" 2. Standard AC")
        print(" 3. 3-Bed Non-AC")
        print(" 4. 3-Bed AC")
        print("\t\tPress 0 for Room Prices")

        try:
            ch = int(input("->"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            Booking()

        if ch == 0:
            print(" 1. Standard Non-AC - Rs. 3500")
            print(" 2. Standard AC - Rs. 4000")
            print(" 3. 3-Bed Non-AC - Rs. 4500")
            print(" 4. 3-Bed AC - Rs. 5000")
            try:
                ch = int(input("->"))
            except ValueError:
                print("Invalid input. Please enter a number.")
                Booking()

        if ch == 1:
            room.append('Standard Non-AC')
            print("Room Type- Standard Non-AC")
            price.append(3500)
            print("Price- 3500")
        elif ch == 2:
            room.append('Standard AC')
            print("Room Type- Standard AC")
            price.append(4000)
            print("Price- 4000")
        elif ch == 3:
            room.append('3-Bed Non-AC')
            print("Room Type- 3-Bed Non-AC")
            price.append(4500)
            print("Price- 4500")
        elif ch == 4:
            room.append('3-Bed AC')
            print("Room Type- 3-Bed AC")
            price.append(5000)
            print("Price- 5000")
        else:
            print(" Wrong choice..!!")

        rn = random.randrange(40) + 300
        cid = random.randrange(40) + 10

        if phn not in phno:
            phno.append(phn)
        else:
            for n in range(0, i):
                if phn == phno[n]:
                    if p[n] == 1:
                        phno.append(phn)

        print("")
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
        print("Room No. - ", rn)
        print("Customer Id - ", cid)
        roomno.append(rn)
        custid.append(cid)
        i = i + 1
        n = int(input("0-BACK\n ->"))
        if n == 0:
            Home()
        else:
            exit()

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit()
    except ValueError as e:
        print("Error:", e)
        exit()


def Rooms_Info():
    print("		 ------ UPESTAYS ROOMS INFO ------")
    print("")
    print("STANDARD NON-AC")
    print("---------------------------------------------------------------")
    print(
        "Room amenities include: 1 Double Bed, Television, Telephone,Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and an attached washroom with hot/cold water.\n")

    print("STANDARD AC")
    print("---------------------------------------------------------------")
    print(
        "Room amenities include: 1 Double Bed, Television, Telephone,Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and an attached washroom with hot/cold water + Window/Split AC.\n")

    print("3-Bed NON-AC")
    print("---------------------------------------------------------------")
    print(
        "Room amenities include: 1 Double Bed + 1 Single Bed, Television, Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1, Side table, Balcony with an Accent table with 2 Chair and an attached washroom with hot/cold water.\n")

    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print(
        "Room amenities include: 1 Double Bed + 1 Single Bed, Television, Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1 Side table, Balcony with an Accent table with 2 Chair and an attached washroom with hot/cold water + Window/Split AC.\n")

    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()


def Record():
    if phno != []:
        print("\t\t*** UPESTAYS RECORD ***\t\t\n")
        print("| Name\t\| Phone No.\t\| Address\t\| Check-In\t| Check-Out\t| Room Type\t| Price\t|")
        print(
            "----------------------------------------------------------------------------------------------------------------------")
        with open("hotel_records.txt", "w") as file:
            file.write("UPESTAYS RECORD\n")
            file.write("| Name\t| Phone No.\t| Address\t| Check-In\t| Check-Out\t| Room Type\t| Price\t|\n")
            file.write(
                "----------------------------------------------------------------------------------------------------------------------\n")

            for n in range(0, i):
                file.write(f"| {name[n]}\t | {phno[n]}\t| {add[n]}\t| {checkin[n]}\t| {checkout[n]}\t| {room[n]}\t| {price[n]}\n")

            file.write(
                "----------------------------------------------------------------------------------------------------------------------\n")
            print("Record saved to hotel_records.txt")
    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
    
        Home()
    else:
        exit()


Home()
