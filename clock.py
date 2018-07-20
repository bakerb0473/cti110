# CTI-110
# Modules-clock
# Bonnita Baker
# 7/5/2018

# This program imports the module calendar
# it will display the full year calendar



def main():

    from time import time, ctime

    prev_time=""
    while True:
        the_time = ctime(time())
        if prev_time != the_time:
            print('The time is:', ctime())
            prev_time = the_time



# Program start
main ()
