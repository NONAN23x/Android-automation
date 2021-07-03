def notification(string, sound="notification1"):
    return f"termux-media-player play Media/{sound} && termux-vibrate -f && termux-notification -t Notification -c \"{string}\" && termux-toast \"{string}\""


def torch(string):
    return f"termux-torch {string}"  # These functions are simplified methods for using system calls


def speak(string):
    return f"termux-tts-speak \"{string}\""


def volume(string):
    return f"termux-volume \"{string}\""


dictionary = {

    "7:0 AM": notification("Wake up"),
    "7:30 AM": notification("Wake up"),
    "8:0 AM": notification("Duolingo"),
    "8:30 AM": notification("Duolingo"),
    "9:0 AM": notification("Workout"),
    "9:30 AM": notification("Workout"),
    "10:0 AM": notification("NOt Assigned"),
    "10:30 AM": notification("Not Assigned"),
    "11:0 AM": notification("TIme Pass"),
    "11:30 AM": notification("Time PAss"),
    "12:0 PM": notification("Time PAss"),
    "12:30 PM": notification("Time PAss"),
    "1:0 PM": notification("Grind Time"),
    "1:30 PM": notification("Grind Time"),
    "2:0 PM": notification("Duolingo"),
    "2:30 PM": notification("Duilingo"),
    "3:0 PM": notification("Anime Time"),
    "3:30 PM": notification("Anime Time"),
    "4:0 PM": notification("Whatever"),
    "4:30 PM": notification("Programming Time"),
    "5:0 PM": notification("Programming Time"),
    "5:30 PM": notification("Programming Time"),
    "6:0 PM": notification("Time for some Onion Routing"),
    "6:30 PM": notification("Onion Routing"),
    "7:0 PM": notification("Nothing SPecial"),
    "7:30 PM": notification("Anime Time"),
    "8:0 PM": notification("Dinner"),
    "8:30 PM": notification("MOre Programming"),
    "9:0 PM": notification("Finishing up the chores"),
    "9:30 PM": notification("Getting ready for bed"),
    "10:0 PM": notification("Anime"),
    "10:30 PM": notification("Pointers out of index")
    "11:0 PM": notification("Go to sleep!")
}
# You can configure this dictionary to your preference
# Simplest yet affective implementation for Android Automation.
