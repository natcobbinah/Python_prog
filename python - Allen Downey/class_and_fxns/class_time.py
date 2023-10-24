class Time:
    """
    Represents the time of the day.

    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 00
time2.minute = 00
time2.second = 30

def print_time(time):
    print('%.2d: %.2d: %.2d' % (time.hour, time.minute, time.second))

def is_after(t1, t2):
    return t1.hour < t2.hour

#print_time(time)
#print(is_after(time, time2))

