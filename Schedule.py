def notification(string, sound="notification1"):
    return f"termux-media-player play Media/{sound} && termux-vibrate -f && termux-notification -t Notification -c \"{string}\""


def torch(string):
    return f"termux-torch {string}"  # These functions are simplified methods for using system calls


def speak(string):
    return f"termux-tts-speak \"{string}\""


def volume(string):
    return f"termux-volume \"{string}\""


dictionary = {

    "5:30 AM": notification("Its's 5:30, wake up"),
    "5:45 AM": notification("Brush your teeth now"),
    "6:0 AM": notification("Workout"),
    "6:30 AM": notification("Now practise"),
    "7:0 AM": notification("It's 7AM"),
    "7:30 AM": notification("Its 7:30 AM"),
    "8:0 AM": notification("Get ready for college"),
    "8:30 AM": notification("You're supposed to be in college now"),
    "9:0 AM": notification("NOthing Special"),
    "9:30 AM": notification("Nothing Special"),
    "10:0 AM": notification("Nothing Special"),
    "10:30 AM": notification("Nothing special"),
    "11:0 AM": notification("Nothing SPecial"),
    "11:30 AM": notification("Its 1130"),
    "12:0 PM": notification("it's 12 AM"),
    "12:30 PM": notification("12:30"),
    "1:0 PM": notification("Time for Prayer"),
    "1:15 PM": notification("Time for Prayer"),
    "1:30 PM": notification("Duolingo Time"),
    "1:45 PM": notification("Duolingo Time"),
    "2:0 PM": notification('Bring some groceries to home'),
    "2:15 PM": notification('Bring some groceries to home'),
    "2:30 PM": notification('Duolingo again'),
    "2:45 PM": notification('Duolingo again'),
    "3:0 PM": notification("Time for some errands"),
    "3:15 PM": notification("Time for some errands"),
    "3:30 PM": notification("Complete your daily chores"),
    "3:45 PM": notification("Complete your daily chores"),
    "4:0 PM": notification("Time for Prayer"),
    "4:15 PM": notification("Time for Prayer"),
    "4:30 PM": notification("Get ready for tuition"),
    "4:45 PM": notification("Get ready for tuition"),
    "5:0 PM": notification("Study well"),
    "5:15 PM": notification("Study well"),
    "5:30 PM": notification("Focus on studying"),
    "5:45 PM": notification("Focus on studying"),
    "6:0 PM": notification("More 60 minutes left"),
    "6:15 PM": notification("More 60 minutes left"),
    "6:30 PM": notification("30 minutes left"),
    "6:45 PM": notification("30 minutes left"),
    "7:0 PM": notification("Errands to run"),
    "7:15 PM": notification("Errands to run"),
    "7:30 PM": notification("Errands to run"),
    "7:45 PM": notification("Errands to run"),
    "8:0 PM": notification("Pharmacy time"),
    "8:15 PM": notification("Pharmacy time"),
    "8:30 PM": notification("Work"),
    "8:45 PM": notification("Work"),
    "9:0 PM": notification("Maybe consider reaching home"),
    "9:15 PM": notification("Maybe consider reaching home"),
    "9:30 PM": notification("Time for some Duolingo"),
    "9:45 PM": notification("Time for some Duolingo"),
    "10:0 PM": notification("Time for some gaming maybe?"),
    "10:15 PM": notification("Time for some gaming maybe?"),
    "10:30 PM": notification("Think of wrapping up things"),
    "10:45 PM": notification("Think of wrapping up things"),
    "11:0 PM": notification("GEt to sleep"),
    "11:30 PM": notification("Sweet dreams"),

}
# You can configure this dictionary to your preference
# Simplest yet affective implementation for Android Automation.
