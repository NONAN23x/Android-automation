#!/bin/python3
import datetime  # This module helps use time
import time  # And this one's for the delay
import os  # Main module that helps run shell commands
import Schedule  # This is a local module
import colorama
cyan = colorama.Fore.CYAN
green = colorama.Fore.GREEN
black = colorama.Fore.BLACK
blue = colorama.Fore.BLUE
red = colorama.Fore.RED
yellow = colorama.Fore.YELLOW
light_green = colorama.Fore.LIGHTGREEN_EX
light_cyan = colorama.Fore.LIGHTCYAN_EX
finish = colorama.Style.RESET_ALL

def main():  # Actual piece of code
    while True:  # True condition for running the program forever
        hour = datetime.datetime.now().hour - 12 if datetime.datetime.now().hour >= 13 else datetime.datetime.now().hour
        # Here 'hour' variable is configured to use 12 hour timezone, if you prefer 24 hours...
        # then tune this logic yourself! ;)
        meridian = " PM" if datetime.datetime.now().hour >= 12 else " AM"  # This is self explanatory
        current_time = str(hour) + ':' + str(datetime.datetime.now().minute) + meridian
        # Actual variable I'll be using to refer to call actual time
        time.sleep(0.5)
        if current_time not in Schedule.dictionary:
            print(light_cyan, current_time, "    (No task)", finish)  # Yes, I use print statements for debugging ;)
        else:
            print(green, current_time, "    Program Executed", finish)
        ###
        try:  # Try and except for dealing with Keyboard Interrupt, for clean code
            if current_time in Schedule.dictionary:
                # And here comes the actual part where python is given decision making privilege
                os.system(Schedule.dictionary[current_time])
                # This is the piece of code that's making system commands
                time.sleep(30)  # sleep method for delaying the process
            else:
                time.sleep(30)
        except KeyboardInterrupt:
            print("\n", red, "^Exit", finish)
            print(red, "Program closed...", finish)
            break
        ###


if __name__ == '__main__':  # Professional way to run a code, right?
    os.system("clear")
    main()
