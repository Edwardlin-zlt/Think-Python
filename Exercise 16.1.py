class Time(object):
    """Represents the time of day.
    attributes: hours, minute, second.
    """
def print_time(time):
    print time.hour
    print time.second
    print time.minute
    print "%.2d : %.2d : %.2d" % (time.hour, time.minute, time.second)

if __name__ == '__main__':
    t = Time()
    t.hour = 14
    t.minute = 16
    t.second = 7
    print_time(t)
