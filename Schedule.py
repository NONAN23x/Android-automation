def notification(string, sound="notification1"):
    return f"termux-media-player play Media/{sound} && termux-vibrate -f && termux-notification -t Notification -c \"{string}\" && termux-toast \"{string}\""


def torch(string):
    return f"termux-torch {string}"  # These functions are simplified methods for using system calls


def speak(string):
    return f"termux-tts-speak \"{string}\""


def volume(string):
    return f"termux-volume \"{string}\""


dictionary = {

    "7:0 AM": notification("Its's 5:30, wake up"),
    "7:30 AM": notification("Its's 5:30, wake up"),
    "8:0 AM": notification("Brush your teeth now"),
    "8:30 AM": notification("Brush your teeth now"),
    "9:0 AM": notification("Workout"),
    "9:30 AM": notification("Workout"),
    "10:0 AM": notification("Now practise"),
    "10:30 AM": notification("Now practise"),
    "11:0 AM": notification("It's 7AM"),
    "11:30 AM": notification("It's 7AM"),
    "12:0 PM": notification("Its 7:30 AM"),
    "12:30 PM": notification("Its 7:30 AM"),
    "1:0 PM": notification("Get ready for college"),
    "1:30 PM": notification("Get ready for college"),
    "2:0 PM": notification("You're supposed to be in college now"),
    "2:30 PM": notification("Get ready for college"),
    "3:0 PM": notification("NOthing Special"),
    "3:30 PM": notification("Get ready for college"),
    "4:0 PM": notification("Nothing Special"),
    "4:30 PM": notification("Get ready for college"),
    "5:0 PM": notification("Nothing Special"),
    "5:30 PM": notification("Get ready for college"),
    "6:0 PM": notification("Nothing special"),
    "6:30 PM": notification("Get ready for college"),
    "7:0 PM": notification("Nothing SPecial"),
    "7:30 PM": notification("Get ready for college"),
    "8:0 PM": notification("Its 1130"),
    "8:30 PM": notification("Get ready for college"),
    "9:0 PM": notification("it's 12 AM"),
    "9:30 PM": notification("Get ready for college"),
    "10:0 PM": notification("12:30"),
    "10:30 PM": notification("Get ready for college")
}
# You can configure this dictionary to your preference
# Simplest yet affective implementation for Android Automation.
