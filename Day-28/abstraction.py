from abc import ABC, abstractmethod

class Payment(ABC):
    def source(self):
        print('Scanner/UPI ID/Mobile number')
    def amount(self):
        print('Enter the amount')
    def bank(self):
        print('select the bank')
    def pin(self):
        print('Enter the pin')
    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print('Success/Fail')

class HDFC(Payment):
    def paymentprocess(self):
        print('You made the payment using HDFC Bank')

class Kotak(Payment):
    def paymentprocess(self):
        print('You made the payment using Kotak Bank')

class ICICI(Payment):
    def paymentprocess(self):
        print('You made the payment using ICICI Bank')

class AXIS(Payment):
    def paymentprocess(self):
        print('You made the payment using AXIS Bank')


nikhil = HDFC()
nikhil.source()
nikhil.amount()
nikhil.bank()
nikhil.pin()
nikhil.paymentprocess()
nikhil.paymentstatus()
print('---------------------------------------')

prasad = Kotak()
prasad.source()
prasad.amount()
prasad.bank()
prasad.pin()
prasad.paymentprocess()
prasad.paymentstatus()
print('----------------------------------------')

tharun = AXIS()
tharun.source()
tharun.amount()
tharun.bank()
tharun.pin()
tharun.paymentprocess()
tharun.paymentstatus()
print('----------------------------------------')

nani = ICICI()
nani.source()
nani.amount()
nani.bank()
nani.pin()
nani.paymentprocess()
nani.paymentstatus()


