def notification(string, sound="notification1"):
    return f"termux-media-player play Media/{sound} && termux-notification -t Notification -c \"{string}\" && termux-toast -b black \"{string}\""


def torch(string):
    return f"termux-torch {string}"  # These functions are simplified methods for using system calls


def speak(string):
    return f"termux-tts-speak \"{string}\""


def volume(string):
    return f"termux-volume \"{string}\""


dictionary = {

    "7:0 AM": notification("Good Morning!"),
    "7:30 AM": notification("Wake up"),
    "8:0 AM": notification("Get ready to Workout"),
    "8:30 AM": notification("Workout"),
    "9:0 AM": notification("Tiem for some Duolingo"),
    "9:30 AM": notification("Time for some Duolingo"),
    "10:0 AM": notification("Grind Time"),
    "10:30 AM": notification("Grind time"),
    "11:0 AM": notification("Read PicoPrimer"),
    "11:30 AM": notification("Time PAss"),
    "12:0 PM": notification("Time PAss"),
    "12:30 PM": notification("Time PAss"),
    "1:0 PM": notification("Grinding Time"),
    "1:30 PM": notification("Grinding Time"),
    "2:0 PM": notification("Duolingo"),
    "2:30 PM": notification("Time for some Malware Analysis"),
    "3:0 PM": notification("Anime Time"),
    "3:30 PM": notification("Anime Time"),
    "4:0 PM": notification("Take some break"),
    "4:30 PM": notification("Daily Tryhackme CTF streak"),
    "5:0 PM": notification("Programming Time"),
    "5:30 PM": notification("Programming Time"),
    "6:0 PM": notification("Time for some Onion Routing"),
    "6:30 PM": notification("Onion Routing"),
    "7:0 PM": notification("Time for some break"),
    "7:30 PM": notification("Do some of c pointers"),
    "8:0 PM": notification("Dinner"),
    "8:30 PM": notification("Read something productive"),
    "9:0 PM": notification("Don't Look at the screen too much!"),
    "9:30 PM": notification("Have you completed your duonlingo lession today?"),
    "10:0 PM": notification("Its already 10, wrap up your work, if pending..."),
    "10:30 PM": notification("Anime time"),
    "11:0 PM": notification("Its time to sleep already")
}
# You can configure this dictionary to your preference
# Simplest yet affective implementation for Android Automation.
