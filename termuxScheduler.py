
def notification(string):
    return "termux-notification -c Notification -t " + string
def toast(string):
    return "termux-toast -b black -c white " + string
def torch(string):
    return "termux-torch" + string               # These functions are simplified methods for using system calls
def speak(string):
    return "termux-tts-speak" + string
def volume(string):
    return "termux-volume" + string

dictionary = {

    "5:30 AM": toast("Hello"),
    "6:0 AM": toast("Hello"),
    "6:30 AM": toast("ITs 630"),
    "7:0 AM": notification("Its 7 o clock"),
    "7:30 AM": " ",
    "8:0 AM": " ",
    "8:30 AM": " ",
    "9:0 AM": " ",
    "9:30 AM": " ",
    "10:0 AM": " ",
    "10:30 AM": " ",
    "11:0 AM": " ",
    "11:30 AM": " ",
    "12:0 PM": " ",
    "12:30 PM": " ",
    "1:0 PM": " ",
    "1:30 PM": " ",
    "2:0 PM": " ",
    "2:30 PM": " ",
    "3:0 PM": " ",
    "3:30 PM": " ",
    "4:0 PM": " ",
    "4:30 PM": " ",
    "5:0 PM": " ",
    "5:30 PM": notification(" LOL 530"),
    "6:0 PM": notification("LOl 600"),
    "6:30 PM": notification("LOL 630"),
    "7:0 PM": notification("LOL 7"),
    "7:30 PM": notification("LOL 730"),
    "8:0 PM": notification("LOL 8"),
    "8:30 PM": notification("LOL 830"),
    "9:0 PM": notification("LOL 9"),
    "9:30 PM": notification("LOL 930"),
    "10:0 PM": notification("LOL 10"),
    "10:30 PM": notification("LOL 1030"),
    "11:0 PM": notification("LOL 11"),
    "11:30 PM": notification("GEt back home you fool"),

}
# You can configure this dictionary to your preference
# Simplest yet affective implementation for Android Automation.
