class Vehicle:
    
    #CONSTUCTOR
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
#Object creation
tesla = Vehicle(180,0)
lambo = Vehicle(350,6)

# access the variables inside init method
print("Tesla Max Speed:",tesla.max_speed)
print("Tesla Mileage:",tesla.mileage)

print()
print("Lamborghini Max Speed:",lambo.max_speed)
print("Lamborghini Mileage:",lambo.mileage)

