class Hotstar:
    def __init__(self,name):
        print(f'Welcome to Hotstar, {name}--------------')
    def auth(self):
        print('You can login/register')
    def dashboard(self):
        print('You can see the dashboard')
    def search(self):
        print('You can search')
    def history(self):
        print('You can see the history')
    def playcontrol(self):
        print('You can Pause/Resume/Play')
    def ads(self):
        print('You will see ads')
    def quality(self):
        print('You can see in low quality')
    def devices(self):
        print('single device')
    def download(self):
        print('You cant download')
    def access(self):
        print('You can access limited content')

class PremiumHotstar(Hotstar):
    def __init__(self,name):
        print(f'Welcome to the Premium Hotstar, {name}-----------')
    def ads(self):
        print('You will not see ads')
    def quality(self):
        print('You can see in high quality')
    def devices(self):
        print('multiple device')
    def download(self):
        print('You can download')
    def access(self):
        print('You can access unlimited content')

prasad = Hotstar('prasad')
prasad.auth()
prasad.dashboard()
prasad.search()
prasad.history()
prasad.playcontrol()
prasad.ads()
prasad.quality()
prasad.devices()
prasad.download()
prasad.access()

nikhil = PremiumHotstar('Nikhil')
nikhil.auth()
nikhil.dashboard()
nikhil.search()
nikhil.history()
nikhil.playcontrol()
nikhil.ads()
nikhil.quality()
nikhil.devices()
nikhil.download()
nikhil.access()

