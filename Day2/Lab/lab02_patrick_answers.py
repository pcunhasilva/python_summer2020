class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod # Class decorator
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    def __str__(self):
        if self.hour in range(0, 10):
            if self.minutes in range(0, 10):
                return "0"+str(self.hour)+":""0"+str(self.minutes)
            else:
                return "0"+str(self.hour)+":"+str(self.minutes)
        else:
            if self.minutes in range(0, 10):
                return str(self.hour)+":""0"+str(self.minutes)
            else:
                return str(self.hour)+":"+str(self.minutes)


    def __add__(self, minutes):
        total_min = minutes + self.minutes
        if total_min <= 59:
            return Clock(abs(self.hour), total_min)
        else:
            addHours = total_min // 60
            new_hour = self.hour + addHours
            hour_times = new_hour // 24
            if hour_times == 1:
                self.hour = abs(new_hour - 24) 
                self.minutes = total_min % 60
            else:
                new_hour = new_hour - (hour_times * 24)
                self.hour = abs(new_hour) 
                self.minutes = total_min % 60

    def __sub__(self, minutes):
        total_min = self.minutes - minutes
        if total_min > 0:
            return Clock(abs(self.hour), total_min)
        else:
            subHours = total_min // 60
            new_hour = self.hour + subHours
            hour_times = abs(new_hour // 24)
            if hour_times == 1:
                new_hour = hour_times - 24
                self.hour = abs(new_hour)
                self.minutes = total_min % 60
            else:
                new_hour = new_hour - (hour_times * 24)
                self.hour = abs(new_hour)
                self.minute = total_min % 60

    def __eq__(self, other):
        return True if (self.hour == other.hour) and (self.minutes == other.minutes) else False

    def __ne__(self, other):
        return False if (self.hour == other.hour) and (self.minutes == other.minutes) else True

clock1 = Clock.at(23, 5)
clock1b = Clock(23, 5)
print(clock1)
print(clock1b)
clock2 = Clock(12, 45)
print(clock2)
clock3 = Clock(12, 45)
print(clock3)

print(clock1 == clock2) ## False
print(clock1 != clock2) ## True
print(clock2 == clock3) ## True

print("testing addition")
clock1 + 60
print(clock1)
print(clock1 == Clock(0, 5))

print("testing subtraction")
clock1 - 100
print(clock1)

