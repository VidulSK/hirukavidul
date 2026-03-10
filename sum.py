class Valut:
    def __init__(self,galleons=0,sickles=0,knuts=0):
        self.galleons=galleons
        self.sickles=sickles
        self.knuts=knuts

    def __str__(self):
        return f"{self.galleons} galleons,{self.sickles} sickles,{self.knuts} knuts"

potter=Valut(100,50,25)
weasly=Valut(25,50,25)

galleons=potter.galleons + weasly.galleons
sickles=potter.sickles + weasly.sickles
knuts=potter.knuts + weasly.sickles

total=Valut(galleons,sickles,knuts)

print(potter)
print(weasly)
print(total)


