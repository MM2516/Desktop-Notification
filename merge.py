import requests
import sys
from tkinter import *
from plyer import *
from botWater import *
from news import *
from weather import *
from system import *
from UpcomingEvents import *

class App:
    def __init__(self, master):
        self.master = master
        master.title("Notification Settings")

        # Heading
        self.heading_label = Label(master, text="Which notifications you want to display?", font=("Arial", 14, "bold"), anchor="w", justify=LEFT)
        self.heading_label.pack(fill="x", padx=10, pady=10)

        # Weather notification toggle
        self.weather_var = BooleanVar()
        self.weather_var.set(False)
        self.weather_checkbox = Checkbutton(master, text="Weather Notifications", variable=self.weather_var, command=self.update_notifications, anchor="w", justify=LEFT)
        self.weather_checkbox.pack(anchor="w", padx=10)

        # Water notification toggle
        self.water_var = BooleanVar()
        self.water_var.set(False)
        self.water_checkbox = Checkbutton(master, text="Water Notification", variable=self.water_var, command=self.update_notifications, anchor="w", justify=LEFT)
        self.water_checkbox.pack(anchor="w", padx=10)

        # News notification toggle
        self.news_var = BooleanVar()
        self.news_var.set(False)
        self.news_checkbox = Checkbutton(master, text="News Notification", variable=self.news_var, command=self.update_notifications, anchor="w", justify=LEFT)
        self.news_checkbox.pack(anchor="w", padx=10)

        # Battery notification toggle
        self.battery_var = BooleanVar()
        self.battery_var.set(False)
        self.battery_checkbox = Checkbutton(master, text="Battery Notification", variable=self.battery_var, command=self.update_notifications, anchor="w", justify=LEFT)
        self.battery_checkbox.pack(anchor="w", padx=10)
        
        # CPU usage notification toggle
        self.disk_var = BooleanVar()
        self.disk_var.set(False)
        self.disk_checkbox = Checkbutton(master, text="Disk Space Notification", variable=self.disk_var, command=self.update_notifications, anchor="w", justify=LEFT)
        self.disk_checkbox.pack(anchor="w", padx=10)

        # Heading
        self.heading_label = Label(master, text="Do you want to set remainder?", font=("Arial", 14, "bold"), anchor="w", justify=LEFT)
        self.heading_label.pack(fill="x", padx=10, pady=10)

        # Calender button
        self.UpcomingEvents = Button(master, text="Open",command=self.Upcoming_Events)
        self.UpcomingEvents.pack(anchor="w", padx=10)

        # Quit button
        self.quit_button = Button(master, text="Quit", command=sys.exit)
        self.quit_button.pack(side=LEFT, padx=30, pady=10)

        # Manage button
        self.manage_button = Button(master, text="Manage Notifications")
        self.manage_button.pack(side=RIGHT, padx=30, pady=10)

    def Upcoming_Events(self):
        Events_Window()

    def update_notifications(self):
        if self.weather_var.get():
            notify_weather()
        if self.water_var.get():
            notify_water()
        if self.news_var.get():
            notify_news()
        if self.battery_var.get():
            notify_battery()
        if self.disk_var.get():
            notify_disk_usage()

with open("file.txt", "w") as f:
    root = Tk()
    root.geometry("600x400+100+100")
    app = App(root)
    root.mainloop()
