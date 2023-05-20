from plyer import notification


def notify_water():
    title = "Drink water"
    message = "Keep yourself hydrated"
    notification.notify(title=title, message=message, app_icon=None, timeout=1, toast=False)
    with open('file.txt', 'r') as f:
        line_count = sum(1 for line in f)
    with open('file.txt', 'a') as f:
        f.write(f"{line_count + 1},Water Remainder, Drink Water, Water, Predefined,Low\n")

#notify_water()