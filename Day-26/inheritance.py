class Telegramv1:
    def message(self):
        print('You can send messages')

class Telegramv2(Telegramv1):
    def status(self):
        print('You can upload your story')

class Telegramv3(Telegramv2):
    def groups(self):
        print('You can create or join a groups with multiple people')

class Telegramv4:
    def community(self):
        print('You can join or create Communities')

class Telegramv5(Telegramv3,Telegramv4):
    def calling(self):
        print('You can Call your Friends now')

class Telegramv6(Telegramv1):
    def videocall(self):
        print('You can Video call your freinds now')


nikhil = Telegramv1()
nikhil.message()

prasad = Telegramv2() #single inheritance
prasad.message()
prasad.status()

tharun = Telegramv3() #multilevel inheritance
tharun.message() 
tharun.status()
tharun.groups()

ramesh = Telegramv5() #multiple inheritance
ramesh.message()
ramesh.status()
ramesh.groups()
ramesh.community()
ramesh.calling()

nani = Telegramv6() #hierarchical inheritance
nani.message()
nani.videocall()