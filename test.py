class Time(object):
    """Represents the time of day.
    attributes: hours, minute, second.
    """

def increment(time,second):
    time.second += second

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    return time

def print_time(time):
    print time.hour
    print time.second
    print time.minute
    print "%.2d : %.2d : %.2d" % (time.hour, time.minute, time.second)

if __name__ == '__main__':
    t1 = Time()
    t1.hour = 14
    t1.minute = 55
    t1.second = 7

    print_time(increment(t1, 55))