import datetime  # This module helps use time
import time  # And this one's for the delay
import os  # Main module that helps run shell commands
import termuxScheduler  # This is a local module


def main():  # Actual piece of code
    while True:  # True condition for running the program forever
        hour = datetime.datetime.now().hour - 12 if datetime.datetime.now().hour >= 13 else datetime.datetime.now().hour
        # Here 'hour' variable is configured to use 12 hour timezone, if you prefer 24 hours...
        # then tune this logic yourself! ;)
        meridian = " PM" if datetime.datetime.now().hour >= 12 else " AM"  # This is self explanatory
        current_time = str(hour) + ':' + str(datetime.datetime.now().minute) + meridian
        # Actual variable I'll be using to refer to call actual time
        if current_time not in termuxScheduler.dictionary:
            print(current_time, "    (no task was assigned)")  # Yes, I use print statements for debugging ;)
        else:
            print(current_time, termuxScheduler.dictionary[current_time])
        ###
        try:  # Try and except for dealing with Keyboard Interrupt, for clean code
            if current_time in termuxScheduler.dictionary:
                # And here comes the actual part where python is given decision making privilege
                os.system(termuxScheduler.dictionary[current_time])
                # This is the piece of code that's making system commands
                time.sleep(40)  # sleep method for delaying the process
            else:
                time.sleep(30)
        except KeyboardInterrupt:
            print("^Exit")
            print("Exiting...")
            break
        ###


if __name__ == '__main__':  # Professional way to run a code, right?
    main()
