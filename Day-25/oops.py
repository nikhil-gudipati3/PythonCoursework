class Flipkart:
    discount = 30

    @classmethod
    def updateddicount(cls):
        cls.discount = 40
        print('Updated Discount: ',cls.discount)

    def info(self,name,phno,address):
        self.name = name
        self.phno = phno
        self.add = address
        print('Welcome to Flipkart',self.name)

    @staticmethod
    def banner():
        print(f'{Flipkart.discount}% is going on, Hurry Now!.....')


nani = Flipkart()
nani.updateddicount()
nani.banner()
nani.info('nani',987654321,'Jubilee')
bhaai = Flipkart()
bhaai.info('Bhaai',0000000000,'Erragadda')
thalapathy = Flipkart()
thalapathy.info('Thalapathy',9999999999,'Tamil Nadu')


