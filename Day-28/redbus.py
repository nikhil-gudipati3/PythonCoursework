class Redbus:
    bus = {i: 'Available' for i in range(1,11)}

    def displayseats(self):
        print('---------EXPRESS BUS----------')
        for i in Redbus.bus:
            print(i,Redbus.bus[i])

    def booking(self,seatno):
        for i in Redbus.bus:
            if i == seatno and Redbus.bus[i] == 'Available':
                Redbus.bus[i] = 'Booked'
                print(f'Your have successfully booked your seat: {seatno}')
                break
        else:
            print(f'{seatno} is already booked')


class User(Redbus):
    def __init__(self,name,email,phno):
        self.name = name
        self.email = email
        self.phno = phno
        print(f'Welcome to Redbus, {self.name}')


nikhil = User('nikhil','nikhil@mail.com','12345567889')
nikhil.displayseats()
nikhil.booking(4)
nikhil.displayseats()

class Driver(Redbus):
    def driverdetails(self):
        self.name = 'Mahesh'
        self.phno = '3244567345'
        self.__address = 'KPHB'
        self.__email = 'mahesh@gmail.com'
        self.__salary = '35000'

    
    

    
