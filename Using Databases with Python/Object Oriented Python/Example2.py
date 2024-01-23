class Partyanimal:
    x=0
    name=""
    def __init__(self,z):
        self.name=z
        print(self.name,"Constructed")
    
    def party(self):
        self.x+=1
        print(self.name,"Party Count",self.x)

s=Partyanimal("Atharv")
s.party()

j=Partyanimal("Tashi")
j.party()
s.party()
