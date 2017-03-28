def what_is_the_time(time_in_mirror):
    # Your code here
    timelist = time_in_mirror.split(":")
    mins = ((int(timelist[1]))%60) + 1
    hours = ((11*int(timelist[0]))%12)
    if hours < 10: hourstr = "0%r" % hours
    else: hourstr = "%r" % hours
    time = hourstr + ":" + str(mins)
    return time

print(what_is_the_time("6:35"))
numbers = [range(0, 12)]

print(numbers)
