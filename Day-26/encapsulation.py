'''
public = inclass, childclass, outside
private = inclass, childclass
protected = inclass, childclass, outside(not recommended)
'''

class Amazon:
    def __init__(self,username,password):
        self.username = username     #public 
        self.__password = password   #private
        self._order = []              #protected
        print(f'Welcome to amazon, {self.username}')

    def getpassword(self): #you have to create seperate method to access private attribute
        return self.__password

    def updatepassword(self,newpassword):
        self.__password = newpassword

    @property
    def accessorder(self):
        return self._order

    @accessorder.setter
    def accessorder(self,neworder):
        self._order.append(neworder)


nikhil = Amazon('nikhil','123456')
print(nikhil.username)
print(nikhil.getpassword())
print(nikhil.accessorder) #it is a property, so no need of ()

nikhil.username = 'nikhilgudipati'
print(nikhil.username)
nikhil.updatepassword('nikhil123')
print(nikhil.getpassword())
nikhil.accessorder = 'suger 1kg'
print(nikhil.accessorder)