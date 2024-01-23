class Partyanimal:
    x=0
    name=""
    def __init__(self,z):
        self.name=z
        print(self.name,"Constructed")
    
    def party(self):
        self.x+=1
        print(self.name,"Party Count",self.x)
class FootballFan(Partyanimal):
    points=0
    def touchdown(self):
        self.points+=7
        self.party()
        print(self.name,"Points",self.points)
s=Partyanimal("Pranav")
s.party()
j=FootballFan("Tashi")
j.party()
j.touchdown()
j.touchdown()
