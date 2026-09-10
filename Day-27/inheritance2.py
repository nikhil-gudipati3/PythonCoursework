class whatsappv1:
    def status(self):
        print('You can upload status for 24hrs')

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print('You can add music and you can react on status')

a = whatsappv1()
a.status()

b = whatsappv2()
b.status

class instagramv1:
    def status(self):
        print('You can upload status for 24hrs')

class instagramv2:
    def status(self):
        print('You can add music and you can react on status')

class instagramv3(instagramv1,instagramv2):
    def status(self):
        instagramv1.status(self)
        instagramv2.status(self)
        print('You can add to cross platform')

a = instagramv1()
a.status()

c = instagramv3()
c.status()


