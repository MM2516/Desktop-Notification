import datetime
import tkinter as tk
from tkinter import messagebox
from win10toast import ToastNotifier
import threading
import time

class UpcomingEvents:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar App")
        self.events = []
        self.event_thread = None

        # create event input fields
        tk.Label(master, text="Event name:").grid(row=0, column=0, padx=5, pady=5)
        self.event_name = tk.Entry(master)
        self.event_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(master, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.event_date = tk.Entry(master)
        self.event_date.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(master, text="Time (HH:MM):").grid(row=2, column=0, padx=5, pady=5)
        self.event_time = tk.Entry(master)
        self.event_time.grid(row=2, column=1, padx=5, pady=5)

        # create event button
        self.add_event_button = tk.Button(master, text="Add Event", command=self.add_event)
        self.add_event_button.grid(row=3, column=1, padx=5, pady=5)

        # create event listbox
        self.event_listbox = tk.Listbox(master)
        self.event_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_event(self):
        event_name = self.event_name.get()
        event_date_str = self.event_date.get()
        event_time_str = self.event_time.get()

        try:
            event_date = datetime.datetime.strptime(event_date_str, "%Y-%m-%d")
            event_time = datetime.datetime.strptime(event_time_str, "%H:%M").time()
            event_datetime = datetime.datetime.combine(event_date, event_time)

            self.events.append((event_name, event_datetime))
            self.event_listbox.insert(tk.END, f"{event_name} ({event_datetime})")
            messagebox.showinfo("Event Added", f"Event '{event_name}' added to calendar.")
            
        except ValueError:
            messagebox.showerror("Invalid Date or Time", "Please enter a valid date and time.")

        # clear input fields
        self.event_name.delete(0, tk.END)
        self.event_date.delete(0, tk.END)
        self.event_time.delete(0, tk.END)

        # start event thread if not already running
        if self.event_thread is None or not self.event_thread.is_alive():
            self.event_thread = threading.Thread(target=self.check_events_thread)
            self.event_thread.start()

    def check_events_thread(self):
        while True:
            now = datetime.datetime.now().replace(second=0, microsecond=0)

            for event in self.events:
                event_name, event_datetime = event

                if event_datetime == now:
                    toaster = ToastNotifier()
                    toaster.show_toast("Calendar App", f"Event '{event_name}' is starting now!", duration=10)

            # wait for one minute before checking again
            time.sleep(60)

def Events_Window():
    root = tk.Tk()
    root.geometry("600x400+100+100")
    UpcomingEvents(root)
    root.mainloop()

Events_Window()