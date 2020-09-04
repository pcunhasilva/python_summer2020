class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    def __str__(self):
        return "%02d:%02d" % (self.hour, self.minutes)
    
    def __add__(self, minutes):
        ## convert everything to minutes
        time_min = self.hour*60 + self.minutes + minutes
        ## 24*60 is minutes in a day
        ## take just the remainder in case it runs over a day
        time_min = time_min % (24*60) 
        self.hour = time_min // 60
        self.minutes = time_min % 60
    
    def __sub__(self, minutes):
        self.__add__(-1*minutes)
        
    def __eq__(self, other):
        return self.hour == other.hour and self.minutes == other.minutes
          
    def __ne__(self, other):
        ## uses the __eq__ function!  
        return not self.__eq__(other)




clock1 = Clock(23, 5)
print(clock1)
clock2 = Clock(12, 45)
print(clock2)
clock3 = Clock(12, 45)
print(clock3)

print(clock1 == clock2) ## False
print(clock1 != clock2) ## True
print(clock2 == clock3) ## True

print("\ntesting addition")
clock1 + 60
print(clock1)
print(clock1 == Clock(0, 5))

print("\ntesting subtraction")
clock1 - 100
print(clock1)

