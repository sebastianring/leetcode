class Person:
    def __init__(self, temp: int, age: int = 30):
        self.temperature = self.setTemperature(temp)
        self.age = age
    
    def setTemperature(self, temp: int):
        if temp < -273.15:
            raise ValueError("Temperature below -273.15")
        else:
            return temp
    
    def getTemperature(self):
        return self.temperature
    

def ifWarm(temp: Person):
    if temp.temperature > 9:
        return True
    else:
        return False

human = Person(37)
serpent = Person(-200)

list1 = []

list1.append(human)
list1.append(serpent)

for p in list1:
    print(p.getTemperature())

r = filter(ifWarm, list1)
for i in r:
    print(i.temperature)

# print(f"warm obj: {r}")