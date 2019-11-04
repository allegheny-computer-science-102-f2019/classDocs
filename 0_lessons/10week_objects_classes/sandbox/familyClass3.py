#create class, remove former Family class's data
class Family():
    pass # class does nothing

myPals = Family() #instance of object
myPals.first_name00 = "Alexander"
myPals.film00 = "Frozen"

myPals.first_name01 = "Daisy"
myPals.likes01 = "Snow"

print("\t ",myPals.first_name00,"and", myPals.film00)
print("\t ",myPals.first_name01,"and", myPals.likes01)
#print("\t ",myPals.first_name01,"and", myPals.film01) #Err!?
