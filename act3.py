class parrot:
    species="bird"
    def __init__(self,name,age):
     self.name=name 
     self.age=age
obj=parrot("blue","6")
print(obj.species)
print(obj.name)
print(obj.age)