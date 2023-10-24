class Time:
    """
    Represents the time of the day
    """

    def __init__(self, hour=0, minute=0, second = 0):
        self.hour = hour
        self.minute = minute 
        self.second = second

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self,seconds):
         time = Time()
         minute, time.second = divmod(seconds,60)
         time.hour, time.minute = divmod(minute,60)
         return time
       
    def increment_time(self, seconds):
        seconds += self.time_to_int()
        return self.int_to_time(seconds)
    
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)
    
    def is_after(self,other):
        return self.time_to_int() > other.time_to_int()

    # addition operator overloading
    """  def __add__(self,other):
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds) """
    
    #using type-based dispatch:
    def __add__(self,other):
        if(isinstance(other,Time)):
            return self.add_time(other)
        else:
            return self.increment_time(other)
    
    # to cater for time_object + number addition only, 
    # __radd__ is used to add it in the reverse operation
    def __radd__(self,other):
        return self.__add__(other)
    
    def __str__(self) :
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)
        

#To make print_time a method, we move it inside the class
#def print_time(time):
#    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

start = Time(9,45)

#print_time(start)

# Now to call print_time, we use the dot notation
#print(start)
#end = start.increment_time(1337)
#print(end)
#print(end.is_after(start))
duration = Time(1,35)
print(start + duration)

# using type-based dispatch to select appropriate method to execute
print(start + 1337) # however this is not commutative

# example
print(1337 + start) # throws error, but resolved with __radd__ operation

#Since Time object supports add operation, sum() can work on its type, eg:
t1 = Time(7,43)
t2 = Time(7,41)
t3 = Time(7,37)
total = sum([t1,t2,t3])
print(total)
