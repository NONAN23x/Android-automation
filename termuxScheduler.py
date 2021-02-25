def notification(string):
    return f"bash termux-notification -t Notification -c '{string}'"


def torch(string):
    return f"bash termux-torch '{string}'"  # These functions are simplified methods for using system calls


def speak(string):
    return f"bash termux-tts-speak '{string}'"


def volume(string):
    return f"bash termux-volume '{string}'"


dictionary = {

    "5:30 AM": notification("LOL"),
    "5:45 AM": notification("s"),
    "6:0 AM": notification("s"),
    "6:30 AM": notification("ITs 630"),
    "7:0 AM": notification("Its 7 o clock"),
    "7:30 AM": notification("wake up"),
    "8:0 AM": notification("Ready up please"),
    "8:30 AM": notification("wake up up"),
    "9:0 AM": notification("It's 9"),
    "9:30 AM": notification("Its 930 "),
    "10:0 AM": notification("It's 10"),
    "10:30 AM": notification("its 1030"),
    "11:0 AM": notification("Its 11"),
    "11:30 AM": notification("Its 1130"),
    "12:0 PM": notification("it's 12 AM"),
    "12:30 PM": notification("12:30"),
    "1:0 PM": notification("1:00"),
    "1:30 PM": notification("LOL its 1:30"),
    "2:0 PM": notification('lol'),
    "2:30 PM": notification('lol'),
    "3:0 PM": notification("lol"),
    "3:30 PM": notification("A"),
    "4:0 PM": notification("g"),
    "4:30 PM": notification("a"),
    "5:0 PM": notification("g"),
    "5:30 PM": notification("LOL 530"),
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
