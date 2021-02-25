def notification(string, lol):
    return f"termux-notification -t Notification -c '{string}'"


def torch(string):
    return f"termux-torch '{string}'"  # These functions are simplified methods for using system calls


def speak(string):
    return f"termux-tts-speak '{string}'"


def volume(string):
    return f"termux-volume '{string}'"


dictionary = {

    "5:30 AM": notification("LOL", "LOL"),
    "5:45 AM": notification("s", "lol"),
    "6:0 AM": notification("s", 's'),
    "6:30 AM": notification("ITs 630", "s"),
    "7:0 AM": notification("Its 7 o clock", "LLOL"),
    "7:30 AM": notification("wake up", "lol"),
    "8:0 AM": notification("Ready up please", "lol"),
    "8:30 AM": notification("wake up up", "lol"),
    "9:0 AM": notification("It's 9", "lol"),
    "9:30 AM": notification("Its 930 ", "Lol"),
    "10:0 AM": notification("It's 10", "lolls"),
    "10:30 AM": notification("its 1030", "lll"),
    "11:0 AM": notification("Its 11", 's'),
    "11:30 AM": notification("Its 1130", 's'),
    "12:0 PM": notification("it's 12 AM", 's'),
    "12:30 PM": notification("12:30", 's'),
    "1:0 PM": notification("1:00", 's'),
    "1:30 PM": notification("LOL its 1:30", 's'),
    "2:0 PM": notification('lol', 'lol'),
    "2:30 PM": notification('lol', "lol"),
    "3:0 PM": notification("lol", "lol"),
    "3:30 PM": notification("A", "a"),
    "4:0 PM": notification("g", "ff"),
    "4:30 PM": notification("a", "a"),
    "5:0 PM": notification("g", "fa"),
    "5:30 PM": notification("LOL 530", 'lol'),
    "6:0 PM": notification("LOl 600", 'lol'),
    "6:30 PM": notification("LOL 630", 'lol'),
    "7:0 PM": notification("LOL 7", 'ww'),
    "7:30 PM": notification("LOL 730", 'ww'),
    "8:0 PM": notification("LOL 8", 'ww'),
    "8:30 PM": notification("LOL 830", 'ww'),
    "9:0 PM": notification("LOL 9", 'ww'),
    "9:30 PM": notification("LOL 930", 'ww'),
    "10:0 PM": notification("LOL 10", 'ww'),
    "10:30 PM": notification("LOL 1030", 'ww'),
    "11:0 PM": notification("LOL 11", 'ww'),
    "11:30 PM": notification("GEt back home you fool", 'ww'),

}
# You can configure this dictionary to your preference
# Simplest yet affective implementation for Android Automation.
