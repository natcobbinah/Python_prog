from class_time import Time, print_time

def add_time(t1,t2): # this is a pure fxn bcos it does not mutate objects passed to it
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1 

    return sum

def increment(time, seconds):
    new_time = Time()
    new_time.minute = time.minute
    new_time.hour  = time.hour
    new_time.second = time.second

    new_time.second += seconds
    
    while new_time.second >= 60:
        new_time.second -= 60
        new_time.minute += 1

    while new_time.minute >= 60:
        new_time.minute -= 60
        new_time.hour += 1

    return new_time

# fxn that converts Times to integers
def time_to_int(time):
    minutes = time.hour * 60 + time.minute 
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minute, time.second = divmod(seconds,60)
    time.hour, time.minute = divmod(minute,60)
    return time

def add_time2(time1,time2):
    seconds = time_to_int(time1) + time_to_int(time2)
    return int_to_time(seconds)

def increment2(time,seconds):
    seconds_converted = time_to_int(time)
    seconds_converted += seconds
    return int_to_time(seconds_converted)

def mul_time(time, number_prod):
    seconds = time_to_int(time)*number_prod
    return int_to_time(seconds)

print(time_to_int(int_to_time(3600)) == 3600)

start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
incremented_time = increment2(done,1209)
print_time(mul_time(incremented_time,60))
print_time(incremented_time)
