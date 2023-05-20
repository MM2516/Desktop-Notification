import psutil
from plyer import notification

# Set thresholds for battery percentage and disk usage
BATTERY_THRESHOLD = 100
DISK_THRESHOLD = 0

def notify_battery():
    # Get the current battery status and check if it's below the threshold
    battery = psutil.sensors_battery()
    if battery is not None and battery.percent < BATTERY_THRESHOLD:
        notification.notify(
            title="Battery Usage",
            message=f"Battery level is {battery.percent}%.",
            app_name="System Status",
            timeout=2
        )
        with open('file.txt', 'r') as f:
            line_count = sum(1 for line in f)
        with open('file.txt', 'a') as f:
            f.write(f"{line_count + 1},Battery Update,Current charge is {battery.percent}%,Charge,System,Low\n")

def notify_disk_usage():
    # Get the current disk usage and check if it's above the threshold
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > DISK_THRESHOLD:
        notification.notify(
            title="Disk Usage",
            message=f"Disk usage is {disk_usage.percent}%",
            app_name="System Status",
            timeout=2
        )
        with open('file.txt', 'r') as f:
            line_count = sum(1 for line in f)
        with open('file.txt', 'a') as f:
            f.write(f"{line_count + 1},Disk Update,Current disk usage is {disk_usage.percent}%,Disk storage,System,Low\n")

#notify_battery()
#notify_disk_usage()

