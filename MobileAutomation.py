import datetime
import time
import os
import termuxScheduler


def main():
    while True:
        hour = datetime.datetime.now().hour - 12 if datetime.datetime.now().hour > 13 else datetime.datetime.now().hour
        meridian = " PM" if datetime.datetime.now().hour >= 12 else " AM"
        current_time = str(hour) + ':' + str(datetime.datetime.now().minute) + meridian
        print(current_time)
        if current_time in termuxScheduler.dictionary:
            os.system(termuxScheduler.dictionary[current_time])
            time.sleep(45)
        else:
            time.sleep(35)


if __name__ == '__main__':
    main()
