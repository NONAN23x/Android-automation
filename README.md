# Android-automation    (V 2.8.5)


Just a simple python script to make android os commands

Prerequisites: Termux app, Termux-API, knowledge of linux

Termux is a linux emulator for android devices and is a perfect way to start learning linux on the go
The code in this repository is intented to make use of the freedom the app provides to make system calls using python in android terminal.


# Keep in mind that you need to acquire wavelock to propoerly run this code

Steps to make it work...

1) Downlaod Termux on your android device. ```https://play.google.com/store/apps/details?id=com.termux```
2) Download Termux-api on your android device ```https://play.google.com/store/apps/details?id=com.termux.api```
3) Update sources ```apt-update && apt-upgrade -y```
4) Install python ```apt-install python -y```
5) Install git ```apt install git -y```
6) Install termux-api in shell ```pkg install termux-api```
7) Go to device's application manager, enable all the permissions for the temux app (Google how to do this if you have no idea about android permissions)
8) clone this repo ```git clone https://github.com/NONAN23x/Android-automation```
9) Navigate to this cloned repository ```cd Android-automation```
10) Mark as executable ```chmod +x MobileAutomation.py```
11) Run it ```./MobileAutomation.py```

So that does it.
If you know what to do, you can change the code in ```Scheduling.py``` to fit your desired time table
The functionality implemented here is not limited to what it semms
The power of python can be used to even handle machine learning algorithms on your handheld device
If you're intrested, visit termux wiki and see the immense functionality the app has to offer.


Termux official website: ```https://termux.com/```\
Termux wiki: ```https://wiki.termux.com/wiki/Main_Page```\
Termux API wiki: ```https://wiki.termux.com/wiki/Termux:API```
